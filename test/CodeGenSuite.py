import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    
    # # # # ---------------------------- TEST PRINT LITERAL ---------------------
    # def test501(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [IntegerLit(1)])
    #         ]))
    #     ])
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 501))

    # def test502(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('writeFloat', [FloatLit(2.0)])
    #         ]))
    #     ])
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 502))

    # def test503(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BooleanLit(True)])
    #         ]))
    #     ])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 503))

    # def test504(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printString', [StringLit('Hello World')])
    #         ]))
    #     ])
    #     expect = "Hello World"
    #     self.assertTrue(TestCodeGen.test(input, expect, 504))

    # # # # ------------------------- TEST BIN EXPR -------------------------
    # def test505(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [BinExpr('+', IntegerLit(1), IntegerLit(2))])
    #         ]))
    #     ])
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input, expect, 505))

    # def test506(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('writeFloat', [BinExpr('+', FloatLit(1.0), FloatLit(2.0))])
    #         ]))
    #     ])
    #     expect = "3.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 506))

    # def test507(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('writeFloat', [BinExpr('-', FloatLit(3.0), IntegerLit(1))])
    #         ]))
    #     ])
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 507))

    # def test508(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [BinExpr('*', IntegerLit(3), IntegerLit(3))])
    #         ]))
    #     ])
    #     expect = "9"
    #     self.assertTrue(TestCodeGen.test(input, expect, 508))

    # def test509(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('writeFloat', [BinExpr('/', IntegerLit(3), IntegerLit(3))])
    #         ]))
    #     ])
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 509))

    # def test510(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('writeFloat', [BinExpr('*', FloatLit(2.5), IntegerLit(4))])
    #         ]))
    #     ])
    #     expect = "10.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 510))

    # def test511(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [BinExpr('%', IntegerLit(10), IntegerLit(3))])
    #         ]))
    #     ])
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 511))

    # # # # # ------------------ TEST REOP --------------------------------------
    # # # # ------------------------- TEST == --------------------------------
    # def test512(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('==', IntegerLit(10), IntegerLit(3))]),
    #             CallStmt('printBoolean', [BinExpr('==', IntegerLit(10), IntegerLit(10))]),
    #         ]))
    #     ])
    #     expect = "falsetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 512))

    # def test513(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('==', BooleanLit(True), BooleanLit(True))]),
    #             CallStmt('printBoolean', [BinExpr('==', BooleanLit(True), BooleanLit(False))]),
    #         ]))
    #     ])
    #     expect = "truefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 513))

    # def test514(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('==', IntegerLit(1), BooleanLit(True))]),
    #             CallStmt('printBoolean', [BinExpr('==', IntegerLit(0), BooleanLit(False))]),
    #         ]))
    #     ])
    #     expect = "truetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 514))

    # # # # ------------------------- TEST != -------------------------------------------
    # def test515(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('!=', IntegerLit(10), IntegerLit(3))]),
    #             CallStmt('printBoolean', [BinExpr('!=', IntegerLit(10), IntegerLit(10))]),
    #         ]))
    #     ])
    #     expect = "truefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 515))

    # def test516(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('!=', BooleanLit(True), BooleanLit(True))]),
    #             CallStmt('printBoolean', [BinExpr('!=', BooleanLit(True), BooleanLit(False))]),
    #         ]))
    #     ])
    #     expect = "falsetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 516))

    # def test517(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('!=', IntegerLit(1), BooleanLit(True))]),
    #             CallStmt('printBoolean', [BinExpr('!=', IntegerLit(0), BooleanLit(False))]),
    #         ]))
    #     ])
    #     expect = "falsefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 517))

    # # # # --------------------------TEST < ---------------------------------------
    # def test518(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('<', IntegerLit(1), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('<', IntegerLit(2), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('<', IntegerLit(3), IntegerLit(2))]),

    #             CallStmt('printBoolean', [BinExpr('<', FloatLit(1.0), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('<', FloatLit(2.0), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('<', FloatLit(3.0), FloatLit(2.0))]),
    #         ]))
    #     ])
    #     expect = "truefalsefalsetruefalsefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 518))

    # def test519(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('<', IntegerLit(1), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('<', FloatLit(2.0), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('<', IntegerLit(3), FloatLit(2.0))]),
    #         ]))
    #     ])
    #     expect = "truefalsefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 519))

    # # # # ------------------------------- Test <= --------------------------------------
    # def test520(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('<=', IntegerLit(1), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('<=', IntegerLit(2), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('<=', IntegerLit(3), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('<=', FloatLit(1.0), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('<=', FloatLit(2.0), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('<=', FloatLit(3.0), FloatLit(2.0))]),
    #         ]))
    #     ])
    #     expect = "truetruefalsetruetruefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 520))

    # def test521(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('<=', IntegerLit(1), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('<=', FloatLit(2.0), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('<=', IntegerLit(3), FloatLit(2.0))]),
    #         ]))
    #     ])
    #     expect = "truetruefalse"
    #     self.assertTrue(TestCodeGen.test(input, expect, 521))

    # # # # ---------------------------- Test > ---------------------------------------
    # def test522(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('>', IntegerLit(1), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('>', IntegerLit(2), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('>', IntegerLit(3), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('>', FloatLit(1.0), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('>', FloatLit(2.0), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('>', FloatLit(3.0), FloatLit(2.0))]),
    #         ]))
    #     ])
    #     expect = "falsefalsetruefalsefalsetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 522))

    # def test523(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('>', IntegerLit(1), FloatLit(2.0))]),
    #             CallStmt('printBoolean', [BinExpr('>', FloatLit(2.0), IntegerLit(2))]),
    #             CallStmt('printBoolean', [BinExpr('>', IntegerLit(3), FloatLit(2.0))]),
    #         ]))
    #     ])
    #     expect = "falsefalsetrue"
    #     self.assertTrue(TestCodeGen.test(input, expect, 523))

    # # # # ------------------------------- TEST AND OR ------------------------------------
    # def test524(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('&&', BooleanLit(True), BooleanLit(True))]),
    #         ]))
    #     ])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 524))

    # def test525(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('&&', BooleanLit(True), BinExpr('&&', BooleanLit(True), BooleanLit(False)))]),
    #         ]))
    #     ])
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 525))

    # def test526(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('&&', BooleanLit(True), BinExpr('&&', BooleanLit(True), BinExpr('&&', BooleanLit(True), BooleanLit(True))))]),
    #         ]))
    #     ])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 526))

    # def test527(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('||', BooleanLit(True), BooleanLit(False))]),
    #         ]))
    #     ])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 527))

    # def test528(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('||', BooleanLit(True), BinExpr('||', BooleanLit(True), BooleanLit(False)))]),
    #         ]))
    #     ])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 528))

    # def test529(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [BinExpr('||', BooleanLit(False), BinExpr('||', BinExpr('||', BooleanLit(False), BooleanLit(False)), BooleanLit(False)))]),
    #         ]))
    #     ])
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 529))

    # # # # ---------------------------- test :: --------------------------------------------
    # def test530(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printString', [BinExpr('::', StringLit('abc'), StringLit('123'))]),
    #         ]))
    #     ])
    #     expect = "abc123"
    #     self.assertTrue(TestCodeGen.test(input, expect, 530))

    # def test531(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printString', [BinExpr('::', StringLit('789'), BinExpr('::', StringLit('456'), StringLit('123')))]),
    #         ]))
    #     ])
    #     expect = "789456123"
    #     self.assertTrue(TestCodeGen.test(input, expect, 531))

    # # # # ----------------- UNEXPR ---------------------------------------
    # def test532(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [UnExpr('-', IntegerLit(5))]),
    #         ]))
    #     ])
    #     expect = "-5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 532))

    # def test533(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('writeFloat', [UnExpr('-', FloatLit(1.0))]),
    #         ]))
    #     ])
    #     expect = "-1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 533))

    # def test534(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('writeFloat', [UnExpr('-', UnExpr('-', FloatLit(1.0)))]),
    #         ]))
    #     ])
    #     expect = "1.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 534))

    # def test535(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [UnExpr('!', BooleanLit(True))]),
    #         ]))
    #     ])
    #     expect = "false"
    #     self.assertTrue(TestCodeGen.test(input, expect, 535))

    # def test536(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printBoolean', [UnExpr('!', UnExpr('!', BooleanLit(True)))]),
    #         ]))
    #     ])
    #     expect = "true"
    #     self.assertTrue(TestCodeGen.test(input, expect, 536))


    # # # # ----------------------- Test VarDecl + visit Id -------------------------------------------
    # def test537(self):
    #     input = Program([
    #         VarDecl('x', IntegerType(), IntegerLit(1)),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [Id('x')]),
    #         ]))
    #     ])
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 537))

    # def test538(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', FloatType(), FloatLit(1.2)),
    #             CallStmt('writeFloat', [Id('x')]),
    #         ]))
    #     ])
    #     expect = "1.2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 538))

    # def test539(self):
    #     input = Program([
    #         VarDecl('x', StringType(), StringLit('abc')),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', StringType(), StringLit('def')),
    #             CallStmt('printString', [Id('x')]),
    #         ]))
    #     ])
    #     expect = "def"
    #     self.assertTrue(TestCodeGen.test(input, expect, 539))

    # def test540(self):
    #     input = Program([
    #         VarDecl('x', IntegerType(), IntegerLit(1)),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('y', IntegerType(), IntegerLit(3)),
    #             CallStmt('printInteger', [BinExpr('+', Id('x'), Id('y'))]),
    #         ]))
    #     ])
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 540))

    # def test541(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [BinExpr('*', Id('x'), Id('y'))]),
    #         ])),
    #         VarDecl('x', IntegerType(), IntegerLit(5)),
    #         VarDecl('y', IntegerType(), IntegerLit(6)),
    #     ])
    #     expect = "30"
    #     self.assertTrue(TestCodeGen.test(input, expect, 541))

    # # # # ----------------------- Test Array Lit And ArrayCell -----------------------------
    # def test542(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', ArrayType([2], IntegerType()), ArrayLit([IntegerLit(2), IntegerLit(3)])),
    #             CallStmt('printInteger', [ArrayCell('a', [IntegerLit(0)])]),
    #         ])),
    #     ])
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 542))

    # def test543(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'a',
    #                 ArrayType([2,3], FloatType()),
    #                 ArrayLit([
    #                     ArrayLit([FloatLit(1.2), FloatLit(5.3), FloatLit(0.8)]),
    #                     ArrayLit([FloatLit(13.4), FloatLit(2.3), FloatLit(4.2)]),
    #                 ])
    #             ),
    #             CallStmt('writeFloat', [ArrayCell('a', [IntegerLit(0), IntegerLit(2)])]),
    #         ])),
    #     ])
    #     expect = "0.8"
    #     self.assertTrue(TestCodeGen.test(input, expect, 543))

    # def test544(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl(
    #                 'a',
    #                 ArrayType([2,3], FloatType()),
    #                 ArrayLit([
    #                     ArrayLit([FloatLit(1.2), FloatLit(5.3), FloatLit(0.8)]),
    #                     ArrayLit([FloatLit(13.4), FloatLit(2.3), FloatLit(4.2)]),
    #                 ])
    #             ),
    #             CallStmt('writeFloat', [BinExpr('+', ArrayCell('a', [IntegerLit(0), IntegerLit(2)]), ArrayCell('a', [IntegerLit(1), IntegerLit(2)]))]),
    #         ])),
    #     ])
    #     expect = "5.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 544))

    # # # # ---------------------  FuncCall --------------------------------------------------------
    # def test545(self):
    #     input = Program([
    #         FuncDecl('printEight', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [IntegerLit(8)]),
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printEight', []),
    #         ])),
    #     ])
    #     expect = "8"
    #     self.assertTrue(TestCodeGen.test(input, expect, 545))

    # # # # # ------------------------------- ParamDecl ----------------------------------------
    # def test546(self):
    #     input = Program([
    #         FuncDecl('printInc', VoidType(), [ParamDecl('n', IntegerType())], None, BlockStmt([
    #             CallStmt('printInteger', [BinExpr('+', Id('n'), IntegerLit(1))]),
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInc', [IntegerLit(1)]),
    #         ])),
    #     ])
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 546))

    # def test547(self):
    #     input = Program([
    #         FuncDecl('printSum', VoidType(), [ParamDecl('x', IntegerType()), ParamDecl('y', IntegerType())], None, BlockStmt([
    #             CallStmt('printInteger', [BinExpr('+', Id('x'), Id('y'))]),
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printSum', [IntegerLit(1), IntegerLit(4)]),
    #         ])),
    #     ])
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 547))

    # def test548(self):
    #     input = Program([
    #         VarDecl('x', IntegerType(), IntegerLit(2)),
    #         FuncDecl('printInt', VoidType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             CallStmt('printInteger', [Id('x')]),
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInt', [IntegerLit(10)]),
    #         ])),
    #     ])
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input, expect, 548))

    # def test549(self):
    #     input = Program([
    #         FuncDecl('foo', VoidType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             CallStmt('printSquare', [BinExpr('+', Id('x'), IntegerLit(1))]),
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('foo', [IntegerLit(1)]),
    #         ])),
    #         FuncDecl('printSquare', VoidType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             CallStmt('printInteger', [BinExpr('*', Id('x'), Id('x'))]),
    #         ])),
    #     ])
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 549))


    # # # # ------------------------------ test AsignStmt -------------------------------------------
    # def test550(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', IntegerType()),
    #             AssignStmt(Id('x'), IntegerLit(10)),
    #             CallStmt('printInteger', [Id('x')]),
    #         ])),
    #     ])
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input, expect, 550))

    # def test551(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', FloatType(), FloatLit(2.3)),
    #             AssignStmt(Id('a'), IntegerLit(123)),
    #             CallStmt('writeFloat', [Id('a')]),
    #         ])),
    #     ])
    #     expect = "123.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 551))

    # def test552(self):
    #     input = Program([
    #         VarDecl('str', StringType(), StringLit('Hello')),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             AssignStmt(Id('str'), BinExpr('::', Id('str'), StringLit(' World'))),
    #             CallStmt('printString', [Id('str')]),
    #         ])),
    #     ])
    #     expect = "Hello World"
    #     self.assertTrue(TestCodeGen.test(input, expect, 552))

    # def test553(self):
    #     input = Program([
    #         VarDecl('n', IntegerType(), IntegerLit(20)),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('s', IntegerType()),
    #             AssignStmt(Id('s'), Id('n')),
    #             CallStmt('printInteger', [Id('s')]),
    #             CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "2020"
    #     self.assertTrue(TestCodeGen.test(input, expect, 553))

    # def test554(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', ArrayType([2], IntegerType()), ArrayLit([IntegerLit(2), IntegerLit(3)])),
    #             AssignStmt(ArrayCell('a', [IntegerLit(0)]), IntegerLit(10)),
    #             CallStmt('printInteger', [ArrayCell('a', [IntegerLit(0)])]),
    #         ])),
    #     ])
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input, expect, 554))

    # def test555(self):
    #     input = Program([
    #         VarDecl('a', ArrayType([2], StringType()), ArrayLit([StringLit('abc'), StringLit('def')])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             AssignStmt(ArrayCell('a', [IntegerLit(0)]), StringLit('123')),
    #             CallStmt('printString', [ArrayCell('a', [IntegerLit(0)])]),
    #         ])),
    #     ])
    #     expect = "123"
    #     self.assertTrue(TestCodeGen.test(input, expect, 555))

    # def test556(self):
    #     input = Program([
    #         VarDecl(
    #             'a',
    #             ArrayType([2,2], StringType()),
    #             ArrayLit([
    #                 ArrayLit([StringLit('abc'), StringLit('def')]), 
    #                 ArrayLit([StringLit('ghi'), StringLit('jkl')]), 
    #             ])
    #         ),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             AssignStmt(ArrayCell('a', [IntegerLit(0), IntegerLit(0)]), ArrayCell('a', [IntegerLit(1), IntegerLit(1)])),
    #             CallStmt('printString', [ArrayCell('a', [IntegerLit(0), IntegerLit(0)])]),
    #         ])),
    #     ])
    #     expect = "jkl"
    #     self.assertTrue(TestCodeGen.test(input, expect, 556))

    # # # # -------------------------- Test IFSTMT -----------------------------------------
    # def test557(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             IfStmt(
    #                 BooleanLit(True),
    #                 CallStmt('printInteger', [IntegerLit(1)]),
    #             ),
    #         ])),
    #     ])
    #     expect = "1"
    #     self.assertTrue(TestCodeGen.test(input, expect, 557))

    # def test558(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('a', BooleanType(), BooleanLit(False)),
    #             IfStmt(
    #                 Id('a'),
    #                 CallStmt('printInteger', [IntegerLit(1)]),
    #                 CallStmt('printInteger', [IntegerLit(0)]),
    #             ),
    #         ])),
    #     ])
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 558))

    # # # # -------------------------- Visit BlockStmt -------------------------------------------
    # def test559(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', IntegerType(), IntegerLit(2)),
    #             VarDecl('a', BooleanType(), BooleanLit(False)),
    #             IfStmt(
    #                 Id('a'),
    #                 BlockStmt([
    #                     VarDecl('x', IntegerType(), IntegerLit(4)),
    #                     CallStmt('printInteger', [Id('x')]),
    #                 ]),
    #                 CallStmt('printInteger', [Id('x')]),
    #             ),
    #         ])),
    #     ])
    #     expect = "2"
    #     self.assertTrue(TestCodeGen.test(input, expect, 559))

    # def test560(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', IntegerType(), IntegerLit(2)),
    #             VarDecl('a', BooleanType(), BooleanLit(False)),
    #             IfStmt(
    #                 Id('a'),
    #                 BlockStmt([
    #                     VarDecl('x', IntegerType(), IntegerLit(10)),
    #                     CallStmt('printInteger', [Id('x')]),
    #                 ]),
    #                 BlockStmt([
    #                     VarDecl('x', IntegerType(), IntegerLit(6)),
    #                     CallStmt('printInteger', [Id('x')]),
    #                 ]),
    #             ),
    #             CallStmt('printInteger', [Id('x')]),
    #         ])),
    #     ])
    #     expect = "62"
    #     self.assertTrue(TestCodeGen.test(input, expect, 560))

    # def test561(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', IntegerType(), IntegerLit(2)),
    #             IfStmt(
    #                 BinExpr('==', Id('x'), IntegerLit(1)),
    #                 BlockStmt([
    #                     VarDecl('x', IntegerType(), IntegerLit(10)),
    #                     CallStmt('printInteger', [Id('x')]),
    #                 ]),
    #                 IfStmt(
    #                     BinExpr('==', Id('x'), IntegerLit(2)),
    #                     BlockStmt([
    #                         VarDecl('x', IntegerType(), IntegerLit(20)),
    #                         CallStmt('printInteger', [Id('x')]),
    #                     ]),
    #                     BlockStmt([
    #                         VarDecl('x', IntegerType(), IntegerLit(30)),
    #                         CallStmt('printInteger', [Id('x')]),
    #                     ]),
    #                 ),
    #             ),
    #         ])),
    #     ])
    #     expect = "20"
    #     self.assertTrue(TestCodeGen.test(input, expect, 561))

    # # # # ----------------------------- While Stmt ---------------------------------
    # def test562(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('x', IntegerType(), IntegerLit(3)),
    #             WhileStmt(
    #                 BinExpr('>', Id('x'), IntegerLit(0)),
    #                 BlockStmt([
    #                     CallStmt('printInteger', [Id('x')]),
    #                     AssignStmt(Id('x'), BinExpr('-', Id('x'), IntegerLit(1)))
    #                 ])
    #             )
    #         ])),
    #     ])
    #     expect = "321"
    #     self.assertTrue(TestCodeGen.test(input, expect, 562))

    # def test563(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType(), IntegerLit(0)),
    #             WhileStmt(
    #                 BinExpr('<', Id('i'), IntegerLit(3)),
    #                 BlockStmt([
    #                     AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i'))),
    #                     AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1))),
    #                 ])
    #             ),
    #             CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input, expect, 563))

    # # # # --------------------------- Break Stmt ---------------------------
    # def test564(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType(), IntegerLit(0)),
    #             WhileStmt(
    #                 BooleanLit(True),
    #                 BlockStmt([
    #                     AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1))),
    #                     AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i'))),
    #                     IfStmt(
    #                         BinExpr('==', Id('i'), IntegerLit(5)),
    #                         BreakStmt()
    #                     )
    #                 ])
    #             ),
    #             CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input, expect, 564))

    # def test565(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType(), IntegerLit(0)),
    #             WhileStmt(
    #                 BooleanLit(True),
    #                 IfStmt(
    #                     BinExpr('==', Id('i'), IntegerLit(3)),
    #                     BreakStmt(),
    #                     BlockStmt([
    #                         AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1))),
    #                         AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i'))),
    #                     ])
    #                 ),
                    
    #             ),
    #             CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "6"
    #     self.assertTrue(TestCodeGen.test(input, expect, 565))

    # def test566(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             WhileStmt(
    #                 BooleanLit(True),
    #                 BlockStmt([
    #                     CallStmt('printInteger', [Id('n')]),
    #                     BreakStmt()
    #                 ])      
    #             ),  
    #         ])),
    #     ])
    #     expect = "0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 566))

    # # # # ------------------ DO WHILE ------------------------------
    # def test567(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             DoWhileStmt(
    #                 BinExpr('<', Id('n'), IntegerLit(5)),
    #                 BlockStmt([
    #                     AssignStmt(Id('n'), BinExpr('+', Id('n'), IntegerLit(1)))
    #                 ])
    #             ),
    #             CallStmt('printInteger', [Id('n')])
    #         ])),
    #     ])
    #     expect = "5"
    #     self.assertTrue(TestCodeGen.test(input, expect, 567))

    # def test568(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType(), IntegerLit(1)),
    #             DoWhileStmt(
    #                 BinExpr('<', Id('i'), IntegerLit(5)),
    #                 BlockStmt([
    #                     AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1))),
    #                     AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i'))),
    #                 ])
    #             ),
    #             CallStmt('printInteger', [Id('n')])
    #         ])),
    #     ])
    #     expect = "14"
    #     self.assertTrue(TestCodeGen.test(input, expect, 568))

    # def test569(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType(), IntegerLit(1)),
    #             DoWhileStmt(
    #                 BooleanLit(True),
    #                 BlockStmt([
    #                     AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i'))),
    #                     AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1))),
    #                     IfStmt(
    #                         BinExpr('>', Id('i'), IntegerLit(5)),
    #                         BreakStmt(),
    #                     ),
    #                 ])
    #             ),
    #             CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "15"
    #     self.assertTrue(TestCodeGen.test(input, expect, 569))

    # # # # --------------------- Continue Stmt ------------------------------------------
    # def test570(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType(), IntegerLit(0)),
    #             DoWhileStmt(
    #                 BinExpr('<', Id('i'), IntegerLit(5)),
    #                 BlockStmt([
    #                     AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1))),
    #                     IfStmt(
    #                         BinExpr('==', Id('i'), IntegerLit(2)),
    #                         ContinueStmt(),
    #                     ),
    #                     AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i'))),
    #                 ])
    #             ),
    #             CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "13"
    #     self.assertTrue(TestCodeGen.test(input, expect, 570))

    # def test571(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType(), IntegerLit(0)),
    #             WhileStmt(
    #                 BinExpr('<', Id('i'), IntegerLit(3)),
    #                 BlockStmt([
    #                     AssignStmt(Id('i'), BinExpr('+', Id('i'), IntegerLit(1))),
    #                     ContinueStmt(),
    #                 ])
    #             ),
    #             CallStmt('printInteger', [Id('i')]),
    #         ])),
    #     ])
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input, expect, 571))

    # # # #  ------------------------ FOR STMT -----------------------------------------
    # def test572(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(3)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 CallStmt('printInteger', [Id('i')]),
    #             ),
    #         ])),
    #     ])
    #     expect = "012"
    #     self.assertTrue(TestCodeGen.test(input, expect, 572))

    # def test573(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(5)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i')))
    #             ),
    #              CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "10"
    #     self.assertTrue(TestCodeGen.test(input, expect, 573))

    # def test574(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(5)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([
    #                     IfStmt(
    #                         BinExpr('==', Id('i'), IntegerLit(2)),
    #                         ContinueStmt()
    #                     ),
    #                     AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i')))
    #                 ])
    #             ),
    #              CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "8"
    #     self.assertTrue(TestCodeGen.test(input, expect, 574))

    # def test575(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(5)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([
    #                     IfStmt(
    #                         BinExpr('==', Id('i'), IntegerLit(3)),
    #                         BreakStmt()
    #                     ),
    #                     AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i')))
    #                 ])
    #             ),
    #              CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input, expect, 575))

    # def test576(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('n', IntegerType(), IntegerLit(0)),
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(100)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([
    #                     IfStmt(
    #                         BinExpr('==', BinExpr('%', Id('i'), IntegerLit(2)), IntegerLit(0)),
    #                         AssignStmt(Id('n'), BinExpr('+', Id('n'), Id('i')))
    #                     ),
    #                 ])
    #             ),
    #              CallStmt('printInteger', [Id('n')]),
    #         ])),
    #     ])
    #     expect = "2450"
    #     self.assertTrue(TestCodeGen.test(input, expect, 576))

    # def test577(self):
    #     input = Program([
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(3)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([
    #                     VarDecl('j', IntegerType()),
    #                     ForStmt(
    #                         AssignStmt(Id('j'), IntegerLit(0)),
    #                         BinExpr('<', Id('j'), IntegerLit(3)),
    #                         BinExpr('+', Id('j'), IntegerLit(1)),
    #                         CallStmt('printInteger', [BinExpr('+', Id('i'), Id('j'))]),
    #                     ),
    #                 ])
    #             ),
    #         ])),
    #     ])
    #     expect = "012123234"
    #     self.assertTrue(TestCodeGen.test(input, expect, 577))

    # def test578(self):
    #     input = Program([
    #         VarDecl(
    #             'arr',
    #             ArrayType([3,3], IntegerType()),
    #             ArrayLit([
    #                 ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]),
    #                 ArrayLit([IntegerLit(10), IntegerLit(20), IntegerLit(30)]),
    #                 ArrayLit([IntegerLit(100), IntegerLit(200), IntegerLit(300)]),
    #             ])
    #         ),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             VarDecl('i', IntegerType()),
    #             ForStmt(
    #                 AssignStmt(Id('i'), IntegerLit(0)),
    #                 BinExpr('<', Id('i'), IntegerLit(3)),
    #                 BinExpr('+', Id('i'), IntegerLit(1)),
    #                 BlockStmt([
    #                     VarDecl('j', IntegerType()),
    #                     ForStmt(
    #                         AssignStmt(Id('j'), IntegerLit(0)),
    #                         BinExpr('<', Id('j'), IntegerLit(3)),
    #                         BinExpr('+', Id('j'), IntegerLit(1)),
    #                         CallStmt('printInteger', [ArrayCell('arr', [Id('i'), Id('j')])]),
    #                     ),
    #                 ])
    #             ),
    #         ])),
    #     ])
    #     expect = "123102030100200300"
    #     self.assertTrue(TestCodeGen.test(input, expect, 578))

    # # # # -------------------------------------- Return Stmt --------------------------------
    # def test579(self):
    #     input = Program([
    #         FuncDecl('inc', IntegerType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             ReturnStmt(BinExpr('+', Id('x'), IntegerLit(1)))
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [FuncCall('inc', [IntegerLit(3)])])
    #         ])),
    #     ])
    #     expect = "4"
    #     self.assertTrue(TestCodeGen.test(input, expect, 579))

    # def test580(self):
    #     input = Program([
    #         FuncDecl('abs', IntegerType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             IfStmt(
    #                 BinExpr('<', Id('x'), IntegerLit(0)),
    #                 ReturnStmt(UnExpr('-', Id('x'))),
    #                 ReturnStmt(Id('x'))
    #             )
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [FuncCall('abs', [UnExpr('-', IntegerLit(3))])])
    #         ])),
    #     ])
    #     expect = "3"
    #     self.assertTrue(TestCodeGen.test(input, expect, 580))

    # def test581(self):
    #     input = Program([
    #         FuncDecl('sqr', IntegerType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             ReturnStmt(BinExpr('*', Id('x'), Id('x')))
    #         ])),
    #         FuncDecl('inc', IntegerType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             ReturnStmt(BinExpr('+', Id('x'), IntegerLit(1)))
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printInteger', [FuncCall('sqr', [FuncCall('inc', [IntegerLit(2)])])])
    #         ])),
    #     ])
    #     expect = "9"
    #     self.assertTrue(TestCodeGen.test(input, expect, 581))

    # def test582(self):
    #     input = Program([
    #         FuncDecl('helloStr', StringType(), [], None, BlockStmt([
    #             ReturnStmt(StringLit('Hello'))
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printString', [FuncCall('helloStr', [])])
    #         ])),
    #     ])
    #     expect = "Hello"
    #     self.assertTrue(TestCodeGen.test(input, expect, 582))

    # def test582(self):
    #     input = Program([
    #         FuncDecl('helloStr', StringType(), [], None, BlockStmt([
    #             ReturnStmt(StringLit('Hello'))
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('printString', [FuncCall('helloStr', [])])
    #         ])),
    #     ])
    #     expect = "Hello"
    #     self.assertTrue(TestCodeGen.test(input, expect, 582))

    # def test583(self):
    #     input = Program([
    #         FuncDecl('float', FloatType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
    #             ReturnStmt(BinExpr('+', FloatLit(0.0), Id('x')))
    #         ])),
    #         FuncDecl('main', VoidType(), [], None, BlockStmt([
    #             CallStmt('writeFloat', [FuncCall('float', [IntegerLit(2)])])
    #         ])),
    #     ])
    #     expect = "2.0"
    #     self.assertTrue(TestCodeGen.test(input, expect, 583))

    def test584(self):
        input = Program([
            FuncDecl('float', FloatType(), [ParamDecl('x', IntegerType())], None, BlockStmt([
                ReturnStmt(BinExpr('+', FloatLit(0.0), Id('x')))
            ])),
            FuncDecl('main', VoidType(), [], None, BlockStmt([
                CallStmt('writeFloat', [FuncCall('float', [IntegerLit(2)])])
            ])),
        ])
        expect = "2.0"
        self.assertTrue(TestCodeGen.test(input, expect, 584))