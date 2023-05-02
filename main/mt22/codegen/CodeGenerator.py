from Emitter import Emitter
from functools import reduce

from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype
    def __str__(self):
        return "MType([{}], {})".format(', '.join([str(item) for item in self.partype]), str(self.rettype))


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return "Symbol(" + self.name + ",\t" + str(self.mtype) + ',\t' + str(self.value) + ")\n"

class FirstCheck(Visitor):
    def __init__(self, className):
        self.className = className
        self.clinit = []
    
    def visitProgram(self, ast, o):
        sym = []
        for decl in ast.decls:
            sym += [self.visit(decl, None)]
        return sym, self.clinit
    def visitVarDecl(self, ast, o):
        if ast.init:
            self.clinit += [AssignStmt(Id(ast.name), ast.init)]
        return Symbol(ast.name, ast.typ, CName(self.className))
    def visitFuncDecl(self, ast, o):
        return Symbol(ast.name, MType([x.typ for x in ast.params], ast.returnType), CName(self.className)) 

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
                ]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, path)
        gc.visit(ast, None)


class SubBody():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst


class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "Index({})".format(self.value)


class CName(Val):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "CName({})".format(self.value)


class CodeGenVisitor(Visitor):
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = "MT22Class"
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.clinitbody = []

    def visitProgram(self, ast, c):
        sym, clinit = FirstCheck(self.className).visitProgram(ast, None)
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        c = SubBody(None, self.env + sym)
        [self.visit(i, c) for i in ast.decls]
        self.genMETHOD(FuncDecl("<init>", None, [], None, BlockStmt([])), c, Frame("<init>", VoidType))
        for stmt in clinit: print(stmt)
        if len(clinit)>0:
            self.genMETHOD(FuncDecl("<clinit>", VoidType(), [], None, BlockStmt(clinit)), sym, Frame("<clinit>", VoidType))
        
        self.emit.emitEPILOG()

        return c

    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name == "main" and len(consdecl.params) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name
        intype = [ArrayType([0], StringType())] if isMain else list(map(lambda x: x.typ, consdecl.params))
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType([0], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:
            local = reduce(lambda env, ele: SubBody(frame, [self.visit(ele, env)]+env.sym), consdecl.params, SubBody(frame, []))
            glenv = local.sym+glenv

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        for stmt in body.body:
            glenv = self.visit(stmt, SubBody(frame, glenv))
            
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType) 
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.params], ast.returnType), CName(self.className))

    def visitVarDecl(self, ast, o):
        if o.frame == None:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name, ast.typ, False))
            return o.sym
        else:
            idx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.name, ast.typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
            if ast.init:
                code, typ = self.visit(ast.init, Access(o.frame, o.sym, False))
                self.emit.printout(code)
                self.emit.printout(self.emit.emitWRITEVAR(ast.name, ast.typ, idx, o.frame))
            o.sym = [Symbol(ast.name, ast.typ, Index(idx))] + o.sym
            return o.sym

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        sym = next(filter(lambda x: ast.name == x.name, nenv), None)
        cname = sym.value.value
        ctype = sym.mtype
        in_ = ("", [])
        for x in ast.args:
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1] + [typ1])
        callmethod = self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame)
        self.emit.printout(in_[0])
        self.emit.printout(callmethod)
        return o.sym

    def visitAssignStmt(self, ast, o):
        rc, rt = self.visit(ast.rhs, Access(o.frame, o.sym, False))
        lc, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True))
        if type(ast.lhs) is ArrayCell:
            self.emit.printout(lc)
            self.emit.printout(rc)
            self.emit.printout(self.emit.emitASTORE(lt, o.frame))
        else:
            self.emit.printout(rc)
            self.emit.printout(lc)
        return o.sym

    def visitBinExpr(self, ast, o):
        e1c, e1t = self.visit(ast.left, o)
        e2c, e2t = self.visit(ast.right, o)
        return e1c + e2c + self.emit.emitADDOP(ast.op, e1t, o.frame), e1t

    def visitUnExpr(self, ast, param): pass # ----------------------------------------------------------------

    def visitId(self, ast, o):
        frame = o.frame
        sym = list(filter(lambda sym: sym.name == ast.name, o.sym))[0]
        if type(sym.value) is CName:
            if o.isLeft:
                return self.emit.emitPUTSTATIC(sym.value.value+'.'+sym.name, sym.mtype, frame), sym.mtype
            else:
                return self.emit.emitGETSTATIC(sym.value.value+'.'+sym.name, sym.mtype, frame), sym.mtype
        else:
            if o.isLeft:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
            else:
                return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, frame), sym.mtype
    
    def visitArrayCell(self, ast, o):
        # ArrayCell('a', [IntegerLit(0), IntegerLit(0)])
        frame = o.frame
        sym = list(filter(lambda sym: sym.name == ast.name, o.sym))[0]
        # SymBol('a', ArrayType([2,2], IntegerType()), Index(1))
        typ = sym.mtype # ArrayType([2, 2], IntegerType())
        loadindex = ''
        if type(sym.value) is CName:
            aload = self.emit.emitGETSTATIC(sym.value.value+'.'+sym.name, sym.mtype, frame)            
        else:
            aload = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, frame)
        for index in ast.cell:
            ic, inttype = self.visit(index, Access(frame, o.sym, False))
            loadindex += ic
            cell = typ.dimensions[1:]
            typ = ArrayType(cell, typ.typ) if len(cell)>0 else typ.typ
            if o.isLeft:
                if len(cell)>0:
                    loadindex += self.emit.emitALOAD(typ, frame)
            else:
                loadindex += self.emit.emitALOAD(typ, frame)
        return aload + loadindex, typ

    def visitIntegerLit(self, ast, o):
        return self.emit.emitPUSHICONST(ast.val, o.frame), IntegerType()
    def visitFloatLit(self, ast, o):
        return self.emit.emitPUSHFCONST(ast.val, o.frame), FloatType()
    def visitStringLit(self, ast, o):
        return self.emit.emitPUSHCONST(ast.val, StringType(), o.frame), StringType()
    def visitBooleanLit(self, ast, o):
        if ast.val:
            return self.emit.emitPUSHICONST(1, o.frame), BooleanType()
        else:
            return self.emit.emitPUSHICONST(0, o.frame), BooleanType()
    def visitArrayLit(self, ast, o):
        frame = o.frame
        typ = None
        item = ''
        length = len(ast.explist)
        code = self.emit.emitPUSHICONST(len(ast.explist), frame)
        frame.push()
        for i in range(length):
            item += self.emit.emitDUP(frame)
            item += self.emit.emitPUSHICONST(i, frame)
            c, typ = self.visit(ast.explist[i], Access(frame, o.sym, False))
            item += c
            item += self.emit.emitASTORE(typ, frame)
        code += self.emit.emitNEWARRAY(typ, frame)
        frame.pop()
        code += item
        return code, ArrayType([length], typ)
        
    # def visitIntegerType(self, ast, param): pass
    # def visitFloatType(self, ast, param): pass
    # def visitBooleanType(self, ast, param): pass
    # def visitStringType(self, ast, param): pass
    # def visitArrayType(self, ast, param): pass
    # def visitAutoType(self, ast, param): pass
    # def visitVoidType(self, ast, param): pass


    def visitFuncCall(self, ast, o):
        frame = o.frame
        sym = list(filter(lambda sym: sym.name == ast.name, o.sym))[0]
        argsCode = ''
        for i in ast.args:
            c, t = self.visit(i, Access(frame, o.sym, False))
            argsCode += c
        return argsCode + self.emit.emitINVOKESTATIC(sym.value.value+'.'+sym.name, sym.mtype, frame), sym.mtype

    # def visitBlockStmt(self, ast, param): pass
    # def visitIfStmt(self, ast, param): pass
    # def visitForStmt(self, ast, param): pass
    # def visitWhileStmt(self, ast, param): pass
    # def visitDoWhileStmt(self, ast, param): pass
    # def visitBreakStmt(self, ast, param): pass
    # def visitContinueStmt(self, ast, param): pass
    def visitReturnStmt(self, ast, o):
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:
            code, typ = self.visit(ast.expr, Access(o.frame, o.sym, False))
            self.emit.printout(code)
            self.emit.printout(self.emit.emitRETURN(typ, o.frame))

    def visitParamDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, ast.name, ast.typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        return Symbol(ast.name, ast.typ, Index(idx))