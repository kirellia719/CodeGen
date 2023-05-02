import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    def test1(self):
        input = Program([
            VarDecl('x', IntegerType(), IntegerLit(20)),
            FuncDecl('inc', IntegerType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
                ReturnStmt(BinExpr('+', Id('x'), IntegerLit(1)))
            ])),
            FuncDecl('main', VoidType(), [], None, BlockStmt([
                CallStmt('printInteger', [Id('x')])
            ]))
        ])
        expect = "20"
        self.assertTrue(TestCodeGen.test(input, expect, 501))

