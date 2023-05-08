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
        self.field = []
        self.method = []
    
    def visitProgram(self, ast, o):
        sym = []
        for decl in ast.decls:
            sym += [self.visit(decl, None)]
        return sym, self.clinit,self.field, self.method
    def visitVarDecl(self, ast, o):
        self.field += [ast]
        if ast.init:
            self.clinit += [AssignStmt(Id(ast.name), ast.init)]
        return Symbol(ast.name, ast.typ, CName(self.className))
    def visitFuncDecl(self, ast, o):
        self.method += [ast]
        return Symbol(ast.name, MType([x.typ for x in ast.params], ast.returnType), CName(self.className)) 

class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readInteger", MType(list(), IntegerType()), CName(self.libName)),
                Symbol("printInteger", MType([IntegerType()], VoidType()), CName(self.libName)),
                Symbol("writeFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("printBoolean", MType([BooleanType()], VoidType()), CName(self.libName)),
                Symbol("printString", MType([StringType()], VoidType()), CName(self.libName)),
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

    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        sym, clinit, field, method = FirstCheck(self.className).visitProgram(ast, None)
        c = SubBody(None, self.env + sym)
        [self.visit(i, c) for i in field]
        self.genMETHOD(FuncDecl("<init>", None, [], None, BlockStmt([])), c, Frame("<init>", VoidType))
        [self.visit(i, c) for i in method]
        # for stmt in clinit: print(stmt)
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

        o = SubBody(frame, glenv)
        for stmt in body.body:
            o = self.visit(stmt, o)
            
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        frame = Frame(ast.name, ast.returnType) 
        self.genMETHOD(ast, o.sym, frame)
        return Symbol(ast.name, MType([x.typ for x in ast.params], ast.returnType), CName(self.className))

    def visitVarDecl(self, ast, o):
        if o.frame == None:
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name, ast.typ, False))
        else:
            idx = o.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(idx, ast.name, ast.typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
            if ast.init:
                code, typ = self.visit(ast.init, Access(o.frame, o.sym, False))
                self.emit.printout(code)
                self.emit.printout(self.emit.emitWRITEVAR(ast.name, ast.typ, idx, o.frame))
            o.sym = [Symbol(ast.name, ast.typ, Index(idx))] + o.sym
        return o

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
        callStmt = self.emit.emitINVOKESTATIC(cname + "/" + ast.name, ctype, frame)
        self.emit.printout(in_[0])
        self.emit.printout(callStmt)
        return o

    def visitAssignStmt(self, ast, o):
        if type(ast.lhs) is ArrayCell:
            lc, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True))
            rc, rt = self.visit(ast.rhs, Access(o.frame, o.sym, False))
            if type(lt) is FloatType and type(rt) is IntegerType:
                rc += self.emit.emitI2F(o.frame)
            self.emit.printout(lc)
            self.emit.printout(rc)
            self.emit.printout(self.emit.emitASTORE(lt, o.frame))
        else:
            rc, rt = self.visit(ast.rhs, Access(o.frame, o.sym, False))
            lc, lt = self.visit(ast.lhs, Access(o.frame, o.sym, True))
            if type(lt) is FloatType and type(rt) is IntegerType:
                rc += self.emit.emitI2F(o.frame)
            self.emit.printout(rc)
            self.emit.printout(lc)
        return o

    def visitBlockStmt(self, ast, o):
        frame = o.frame
        frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        newSubBody = SubBody(o.frame, o.sym)
        for i in ast.body:
            newSubBody = self.visit(i, newSubBody)
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        o.frame.exitScope()
        return o

    def visitIfStmt(self, ast, o):
        frame = o.frame
        ec, et = self.visit(ast.cond, Access(frame, o.sym, False))
        self.emit.printout(ec)
        
        falseLabel = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFFALSE(falseLabel, frame))
        self.visit(ast.tstmt, o)
        
        if ast.fstmt is None:
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
        else:
            nextLabel = frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(nextLabel, frame))
            
            self.emit.printout(self.emit.emitLABEL(falseLabel, frame))
            self.visit(ast.fstmt, o)
            
            self.emit.printout(self.emit.emitLABEL(nextLabel, frame))
        return o

    def visitForStmt(self, ast, o):
        self.visit(ast.init, o)

        frame = o.frame
        frame.enterLoop()
        startLabel = frame.getNewLabel()
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(startLabel, frame))

        condCode, condType = self.visit(ast.cond, Access(frame, o.sym, False))
        self.emit.printout(condCode)
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))

        self.visit(ast.stmt, o)

        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        self.visit(AssignStmt(ast.init.lhs, ast.upd), o)
        self.emit.printout(self.emit.emitGOTO(startLabel, frame))

        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        frame.exitLoop()

        return o

    def visitWhileStmt(self, ast, o):
        frame = o.frame
        frame.enterLoop()
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        ec, et = self.visit(ast.cond, Access(frame, o.sym, False))
        self.emit.printout(ec)
        
        self.emit.printout(self.emit.emitIFFALSE(breakLabel, frame))
        self.visit(ast.stmt, o)
        self.emit.printout(self.emit.emitGOTO(continueLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        frame.exitLoop()
        return o

    def visitDoWhileStmt(self, ast, o):
        frame = o.frame
        frame.enterLoop()
        continueLabel = frame.getContinueLabel()
        breakLabel = frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(continueLabel, frame))
        self.visit(ast.stmt, o)
        ec, et = self.visit(ast.cond, Access(frame, o.sym, False))
        self.emit.printout(ec)
        self.emit.printout(self.emit.emitIFTRUE(continueLabel, frame))
        self.emit.printout(self.emit.emitLABEL(breakLabel, frame))
        frame.exitLoop()
        return o

    def visitBreakStmt(self, ast, o):
        breakLabel = o.frame.getBreakLabel()
        self.emit.printout(self.emit.emitGOTO(breakLabel, o.frame))
        return o

    def visitContinueStmt(self, ast, o):
        continueLabel = o.frame.getContinueLabel()
        self.emit.printout(self.emit.emitGOTO(continueLabel, o.frame))
        return o

    def visitReturnStmt(self, ast, o):
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:
            code, typ = self.visit(ast.expr, Access(o.frame, o.sym, False))
            self.emit.printout(code)
            self.emit.printout(self.emit.emitGOTO(o.frame.endLabel[0], o.frame))

    def visitParamDecl(self, ast, o):
        idx = o.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(idx, ast.name, ast.typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
        return Symbol(ast.name, ast.typ, Index(idx))

    def visitBinExpr(self, ast, o):
        lc, lt = self.visit(ast.left, o)
        rc, rt = self.visit(ast.right, o)

        if ast.op in ['+', '-']:
            if type(lt) == type(rt):
                typ = lt
            elif type(lt) is IntegerType:
                lc = lc + self.emit.emitI2F(o.frame)
                typ = FloatType()
            elif type(rt) is IntegerType:
                rc = rc + self.emit.emitI2F(o.frame)
                typ = FloatType()
            code = self.emit.emitADDOP(ast.op, lt, o.frame)
        elif ast.op in ['*']:
            if type(lt) == type(rt):
                typ = lt
            elif type(lt) is IntegerType:
                lc = lc + self.emit.emitI2F(o.frame)
                typ = FloatType()
            elif type(rt) is IntegerType:
                rc = rc + self.emit.emitI2F(o.frame)
                typ = FloatType()
            code = self.emit.emitMULOP(ast.op, typ, o.frame)
            
        elif ast.op in ['/']:
            if type(lt) is IntegerType:
                lc = lc + self.emit.emitI2F(o.frame)
            if type(rt) is IntegerType:
                rc = rc + self.emit.emitI2F(o.frame)
            code = self.emit.emitMULOP(ast.op, FloatType(), o.frame)
            typ = FloatType()

        elif ast.op in ['%']:
            code = self.emit.emitMOD(o.frame)
            typ = IntegerType()
            
        elif ast.op in ['>','<','>=','<=','!=','==']:
            if type(lt) == type(rt):
                typ = lt
            elif type(rt) is FloatType:
                lc = lc + self.emit.emitI2F(o.frame)
                typ = FloatType()
            elif type(lt) is FloatType:
                rc = rc + self.emit.emitI2F(o.frame)
                typ = FloatType()
            elif type(rt) is BooleanType or type(lt) is FloatType:
                typ = BooleanType()
            code = self.emit.emitREOP(ast.op, typ, o.frame)
            typ = BooleanType()
        
        elif ast.op in ['&&']:
            code = self.emit.emitANDOP(o.frame)
            typ = BooleanType()
        elif ast.op in ['||']:
            code = self.emit.emitOROP(o.frame)
            typ = BooleanType()

        elif ast.op in ['::']:
            code = self.emit.emitINVOKEVIRTUAL('java/lang/String/concat', MType([StringType()], StringType()), o.frame)
            typ = StringType()
        return lc + rc + code, typ

    def visitUnExpr(self, ast, o):
        code, typ = self.visit(ast.val, o)
        if ast.op in ['-']:
            code += self.emit.emitNEGOP(typ, o.frame)
        elif ast.op in ['!']:
            code += self.emit.emitNOT(typ, o.frame)
        return code, typ

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

    def visitFuncCall(self, ast, o):
        frame = o.frame
        sym = list(filter(lambda sym: sym.name == ast.name, o.sym))[0]
        argsCode = ''
        for i in ast.args:
            c, t = self.visit(i, Access(frame, o.sym, False))
            argsCode += c
        return argsCode + self.emit.emitINVOKESTATIC(sym.value.value+'.'+sym.name, sym.mtype, frame), sym.mtype

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
        for i in range(length):
            item += self.emit.emitDUP(frame)
            item += self.emit.emitPUSHICONST(i, frame)
            c, typ = self.visit(ast.explist[i], Access(frame, o.sym, False))
            item += c
            item += self.emit.emitASTORE(typ, frame)
        code += self.emit.emitNEWARRAY(typ, frame)
        code += item
        return code, ArrayType([length], typ)
        