# Generated from Aevum.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,35,235,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,3,1,53,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,64,8,3,10,3,12,3,67,9,3,
        1,3,3,3,70,8,3,1,3,3,3,73,8,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,
        5,3,5,84,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,3,7,
        98,8,7,1,8,1,8,1,8,5,8,103,8,8,10,8,12,8,106,9,8,1,8,3,8,109,8,8,
        1,8,3,8,112,8,8,1,9,1,9,1,9,1,9,1,9,1,9,3,9,120,8,9,1,10,1,10,1,
        10,5,10,125,8,10,10,10,12,10,128,9,10,1,10,3,10,131,8,10,1,10,3,
        10,134,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,3,11,147,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,3,11,160,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,5,11,187,8,11,10,11,12,11,190,9,11,1,12,1,12,1,
        12,1,12,1,12,1,12,3,12,198,8,12,1,13,1,13,1,14,1,14,1,15,1,15,1,
        16,1,16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,5,18,216,8,18,10,
        18,12,18,219,9,18,1,18,3,18,222,8,18,1,18,3,18,225,8,18,1,19,1,19,
        1,19,1,19,1,20,1,20,1,20,1,20,1,20,0,1,22,21,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,0,4,1,0,16,17,1,0,18,19,1,
        0,20,25,1,0,29,30,246,0,45,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,72,
        1,0,0,0,8,74,1,0,0,0,10,83,1,0,0,0,12,85,1,0,0,0,14,97,1,0,0,0,16,
        111,1,0,0,0,18,119,1,0,0,0,20,133,1,0,0,0,22,159,1,0,0,0,24,197,
        1,0,0,0,26,199,1,0,0,0,28,201,1,0,0,0,30,203,1,0,0,0,32,205,1,0,
        0,0,34,207,1,0,0,0,36,224,1,0,0,0,38,226,1,0,0,0,40,230,1,0,0,0,
        42,44,3,2,1,0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,
        0,0,0,46,48,1,0,0,0,47,45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,
        53,3,4,2,0,51,53,3,12,6,0,52,50,1,0,0,0,52,51,1,0,0,0,53,3,1,0,0,
        0,54,55,5,1,0,0,55,56,3,26,13,0,56,57,5,2,0,0,57,58,3,6,3,0,58,59,
        5,3,0,0,59,5,1,0,0,0,60,65,3,8,4,0,61,62,5,4,0,0,62,64,3,8,4,0,63,
        61,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,69,1,0,0,
        0,67,65,1,0,0,0,68,70,5,4,0,0,69,68,1,0,0,0,69,70,1,0,0,0,70,73,
        1,0,0,0,71,73,1,0,0,0,72,60,1,0,0,0,72,71,1,0,0,0,73,7,1,0,0,0,74,
        75,3,26,13,0,75,76,5,5,0,0,76,77,3,10,5,0,77,9,1,0,0,0,78,84,3,26,
        13,0,79,80,5,6,0,0,80,81,3,10,5,0,81,82,5,7,0,0,82,84,1,0,0,0,83,
        78,1,0,0,0,83,79,1,0,0,0,84,11,1,0,0,0,85,86,5,8,0,0,86,87,3,26,
        13,0,87,88,5,9,0,0,88,89,3,6,3,0,89,90,5,10,0,0,90,91,3,14,7,0,91,
        92,5,2,0,0,92,93,3,16,8,0,93,94,5,3,0,0,94,13,1,0,0,0,95,96,5,11,
        0,0,96,98,3,10,5,0,97,95,1,0,0,0,97,98,1,0,0,0,98,15,1,0,0,0,99,
        104,3,18,9,0,100,101,5,12,0,0,101,103,3,18,9,0,102,100,1,0,0,0,103,
        106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,108,1,0,0,0,106,
        104,1,0,0,0,107,109,5,12,0,0,108,107,1,0,0,0,108,109,1,0,0,0,109,
        112,1,0,0,0,110,112,1,0,0,0,111,99,1,0,0,0,111,110,1,0,0,0,112,17,
        1,0,0,0,113,114,5,13,0,0,114,115,3,8,4,0,115,116,5,14,0,0,116,117,
        3,22,11,0,117,120,1,0,0,0,118,120,3,22,11,0,119,113,1,0,0,0,119,
        118,1,0,0,0,120,19,1,0,0,0,121,126,3,22,11,0,122,123,5,4,0,0,123,
        125,3,22,11,0,124,122,1,0,0,0,125,128,1,0,0,0,126,124,1,0,0,0,126,
        127,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,129,131,5,4,0,0,130,
        129,1,0,0,0,130,131,1,0,0,0,131,134,1,0,0,0,132,134,1,0,0,0,133,
        121,1,0,0,0,133,132,1,0,0,0,134,21,1,0,0,0,135,136,6,11,-1,0,136,
        137,5,26,0,0,137,138,3,22,11,0,138,139,5,2,0,0,139,140,3,16,8,0,
        140,146,5,3,0,0,141,142,5,27,0,0,142,143,5,2,0,0,143,144,3,16,8,
        0,144,145,5,3,0,0,145,147,1,0,0,0,146,141,1,0,0,0,146,147,1,0,0,
        0,147,160,1,0,0,0,148,149,5,28,0,0,149,150,3,22,11,0,150,151,5,2,
        0,0,151,152,3,16,8,0,152,153,5,3,0,0,153,160,1,0,0,0,154,155,5,9,
        0,0,155,156,3,22,11,0,156,157,5,10,0,0,157,160,1,0,0,0,158,160,3,
        24,12,0,159,135,1,0,0,0,159,148,1,0,0,0,159,154,1,0,0,0,159,158,
        1,0,0,0,160,188,1,0,0,0,161,162,10,8,0,0,162,163,7,0,0,0,163,187,
        3,22,11,9,164,165,10,7,0,0,165,166,7,1,0,0,166,187,3,22,11,8,167,
        168,10,6,0,0,168,169,7,2,0,0,169,187,3,22,11,7,170,171,10,3,0,0,
        171,172,5,14,0,0,172,187,3,22,11,4,173,174,10,11,0,0,174,175,5,6,
        0,0,175,176,3,22,11,0,176,177,5,7,0,0,177,187,1,0,0,0,178,179,10,
        10,0,0,179,180,5,9,0,0,180,181,3,20,10,0,181,182,5,10,0,0,182,187,
        1,0,0,0,183,184,10,9,0,0,184,185,5,15,0,0,185,187,3,26,13,0,186,
        161,1,0,0,0,186,164,1,0,0,0,186,167,1,0,0,0,186,170,1,0,0,0,186,
        173,1,0,0,0,186,178,1,0,0,0,186,183,1,0,0,0,187,190,1,0,0,0,188,
        186,1,0,0,0,188,189,1,0,0,0,189,23,1,0,0,0,190,188,1,0,0,0,191,198,
        3,26,13,0,192,198,3,28,14,0,193,198,3,30,15,0,194,198,3,32,16,0,
        195,198,3,34,17,0,196,198,3,40,20,0,197,191,1,0,0,0,197,192,1,0,
        0,0,197,193,1,0,0,0,197,194,1,0,0,0,197,195,1,0,0,0,197,196,1,0,
        0,0,198,25,1,0,0,0,199,200,5,31,0,0,200,27,1,0,0,0,201,202,7,3,0,
        0,202,29,1,0,0,0,203,204,5,32,0,0,204,31,1,0,0,0,205,206,5,33,0,
        0,206,33,1,0,0,0,207,208,3,26,13,0,208,209,5,2,0,0,209,210,3,36,
        18,0,210,211,5,3,0,0,211,35,1,0,0,0,212,217,3,38,19,0,213,214,5,
        4,0,0,214,216,3,38,19,0,215,213,1,0,0,0,216,219,1,0,0,0,217,215,
        1,0,0,0,217,218,1,0,0,0,218,221,1,0,0,0,219,217,1,0,0,0,220,222,
        5,4,0,0,221,220,1,0,0,0,221,222,1,0,0,0,222,225,1,0,0,0,223,225,
        1,0,0,0,224,212,1,0,0,0,224,223,1,0,0,0,225,37,1,0,0,0,226,227,3,
        26,13,0,227,228,5,5,0,0,228,229,3,22,11,0,229,39,1,0,0,0,230,231,
        5,6,0,0,231,232,3,20,10,0,232,233,5,7,0,0,233,41,1,0,0,0,22,45,52,
        65,69,72,83,97,104,108,111,119,126,130,133,146,159,186,188,197,217,
        221,224
    ]

class AevumParser ( Parser ):

    grammarFileName = "Aevum.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'{'", "'}'", "','", "':'", 
                     "'['", "']'", "'fn'", "'('", "')'", "'->'", "';'", 
                     "'let'", "'='", "'.'", "'*'", "'/'", "'+'", "'-'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'if'", 
                     "'else'", "'while'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENT", "NUMBER", 
                      "STRING", "WS", "COMMENT" ]

    RULE_module = 0
    RULE_declaration = 1
    RULE_struct = 2
    RULE_variable_list = 3
    RULE_variable = 4
    RULE_type = 5
    RULE_function = 6
    RULE_return_type = 7
    RULE_statement_list = 8
    RULE_statement = 9
    RULE_expr_list = 10
    RULE_expr = 11
    RULE_atom = 12
    RULE_identifier = 13
    RULE_boolean_literal = 14
    RULE_numeric_literal = 15
    RULE_string_literal = 16
    RULE_struct_literal = 17
    RULE_field_initialiser_list = 18
    RULE_field_initialiser = 19
    RULE_array_literal = 20

    ruleNames =  [ "module", "declaration", "struct", "variable_list", "variable", 
                   "type", "function", "return_type", "statement_list", 
                   "statement", "expr_list", "expr", "atom", "identifier", 
                   "boolean_literal", "numeric_literal", "string_literal", 
                   "struct_literal", "field_initialiser_list", "field_initialiser", 
                   "array_literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    IDENT=31
    NUMBER=32
    STRING=33
    WS=34
    COMMENT=35

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AevumParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(AevumParser.DeclarationContext,i)


        def getRuleIndex(self):
            return AevumParser.RULE_module

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule" ):
                return visitor.visitModule(self)
            else:
                return visitor.visitChildren(self)




    def module(self):

        localctx = AevumParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==8:
                self.state = 42
                self.declaration()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
            self.match(AevumParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct(self):
            return self.getTypedRuleContext(AevumParser.StructContext,0)


        def function(self):
            return self.getTypedRuleContext(AevumParser.FunctionContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = AevumParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.struct()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.function()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(AevumParser.IdentifierContext,0)


        def variable_list(self):
            return self.getTypedRuleContext(AevumParser.Variable_listContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_struct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct" ):
                return visitor.visitStruct(self)
            else:
                return visitor.visitChildren(self)




    def struct(self):

        localctx = AevumParser.StructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_struct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(AevumParser.T__0)
            self.state = 55
            self.identifier()
            self.state = 56
            self.match(AevumParser.T__1)
            self.state = 57
            self.variable_list()
            self.state = 58
            self.match(AevumParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.VariableContext)
            else:
                return self.getTypedRuleContext(AevumParser.VariableContext,i)


        def getRuleIndex(self):
            return AevumParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = AevumParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_list)
        self._la = 0 # Token type
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.variable()
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 61
                        self.match(AevumParser.T__3)
                        self.state = 62
                        self.variable() 
                    self.state = 67
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 68
                    self.match(AevumParser.T__3)


                pass
            elif token in [3, 10]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(AevumParser.IdentifierContext,0)


        def type_(self):
            return self.getTypedRuleContext(AevumParser.TypeContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = AevumParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.identifier()
            self.state = 75
            self.match(AevumParser.T__4)
            self.state = 76
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AevumParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(AevumParser.TypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)


    class BasicTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(AevumParser.IdentifierContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicType" ):
                return visitor.visitBasicType(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = AevumParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                localctx = AevumParser.BasicTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 78
                self.identifier()
                pass
            elif token in [6]:
                localctx = AevumParser.ArrayTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(AevumParser.T__5)
                self.state = 80
                self.type_()
                self.state = 81
                self.match(AevumParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(AevumParser.IdentifierContext,0)


        def variable_list(self):
            return self.getTypedRuleContext(AevumParser.Variable_listContext,0)


        def return_type(self):
            return self.getTypedRuleContext(AevumParser.Return_typeContext,0)


        def statement_list(self):
            return self.getTypedRuleContext(AevumParser.Statement_listContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = AevumParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(AevumParser.T__7)
            self.state = 86
            self.identifier()
            self.state = 87
            self.match(AevumParser.T__8)
            self.state = 88
            self.variable_list()
            self.state = 89
            self.match(AevumParser.T__9)
            self.state = 90
            self.return_type()
            self.state = 91
            self.match(AevumParser.T__1)
            self.state = 92
            self.statement_list()
            self.state = 93
            self.match(AevumParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(AevumParser.TypeContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_return_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type" ):
                return visitor.visitReturn_type(self)
            else:
                return visitor.visitChildren(self)




    def return_type(self):

        localctx = AevumParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_return_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 95
                self.match(AevumParser.T__10)
                self.state = 96
                self.type_()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.StatementContext)
            else:
                return self.getTypedRuleContext(AevumParser.StatementContext,i)


        def getRuleIndex(self):
            return AevumParser.RULE_statement_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_list" ):
                return visitor.visitStatement_list(self)
            else:
                return visitor.visitChildren(self)




    def statement_list(self):

        localctx = AevumParser.Statement_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement_list)
        self._la = 0 # Token type
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 9, 13, 26, 28, 29, 30, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.statement()
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 100
                        self.match(AevumParser.T__11)
                        self.state = 101
                        self.statement() 
                    self.state = 106
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==12:
                    self.state = 107
                    self.match(AevumParser.T__11)


                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AevumParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AevumParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStatement" ):
                return visitor.visitExprStatement(self)
            else:
                return visitor.visitChildren(self)


    class LetStatementContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(AevumParser.VariableContext,0)

        def expr(self):
            return self.getTypedRuleContext(AevumParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStatement" ):
                return visitor.visitLetStatement(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = AevumParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statement)
        try:
            self.state = 119
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = AevumParser.LetStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(AevumParser.T__12)
                self.state = 114
                self.variable()
                self.state = 115
                self.match(AevumParser.T__13)
                self.state = 116
                self.expr(0)
                pass
            elif token in [6, 9, 26, 28, 29, 30, 31, 32, 33]:
                localctx = AevumParser.ExprStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.ExprContext)
            else:
                return self.getTypedRuleContext(AevumParser.ExprContext,i)


        def getRuleIndex(self):
            return AevumParser.RULE_expr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_list" ):
                return visitor.visitExpr_list(self)
            else:
                return visitor.visitChildren(self)




    def expr_list(self):

        localctx = AevumParser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expr_list)
        self._la = 0 # Token type
        try:
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 9, 26, 28, 29, 30, 31, 32, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.expr(0)
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 122
                        self.match(AevumParser.T__3)
                        self.state = 123
                        self.expr(0) 
                    self.state = 128
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 129
                    self.match(AevumParser.T__3)


                pass
            elif token in [7, 10]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AevumParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AdditionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.ExprContext)
            else:
                return self.getTypedRuleContext(AevumParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddition" ):
                return visitor.visitAddition(self)
            else:
                return visitor.visitChildren(self)


    class MemberAccessContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AevumParser.ExprContext,0)

        def identifier(self):
            return self.getTypedRuleContext(AevumParser.IdentifierContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccess" ):
                return visitor.visitMemberAccess(self)
            else:
                return visitor.visitChildren(self)


    class ComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.ExprContext)
            else:
                return self.getTypedRuleContext(AevumParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)


    class IfElseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AevumParser.ExprContext,0)

        def statement_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.Statement_listContext)
            else:
                return self.getTypedRuleContext(AevumParser.Statement_listContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse" ):
                return visitor.visitIfElse(self)
            else:
                return visitor.visitChildren(self)


    class ParenthicalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AevumParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthicalExpr" ):
                return visitor.visitParenthicalExpr(self)
            else:
                return visitor.visitChildren(self)


    class MultplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.ExprContext)
            else:
                return self.getTypedRuleContext(AevumParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultplication" ):
                return visitor.visitMultplication(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AevumParser.ExprContext,0)

        def expr_list(self):
            return self.getTypedRuleContext(AevumParser.Expr_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)


    class WhileLoopContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AevumParser.ExprContext,0)

        def statement_list(self):
            return self.getTypedRuleContext(AevumParser.Statement_listContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileLoop" ):
                return visitor.visitWhileLoop(self)
            else:
                return visitor.visitChildren(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(AevumParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomExpr" ):
                return visitor.visitAtomExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrayIndexContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.ExprContext)
            else:
                return self.getTypedRuleContext(AevumParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayIndex" ):
                return visitor.visitArrayIndex(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AevumParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.ExprContext)
            else:
                return self.getTypedRuleContext(AevumParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AevumParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = AevumParser.IfElseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 136
                self.match(AevumParser.T__25)
                self.state = 137
                self.expr(0)
                self.state = 138
                self.match(AevumParser.T__1)
                self.state = 139
                self.statement_list()
                self.state = 140
                self.match(AevumParser.T__2)
                self.state = 146
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 141
                    self.match(AevumParser.T__26)
                    self.state = 142
                    self.match(AevumParser.T__1)
                    self.state = 143
                    self.statement_list()
                    self.state = 144
                    self.match(AevumParser.T__2)


                pass
            elif token in [28]:
                localctx = AevumParser.WhileLoopContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(AevumParser.T__27)
                self.state = 149
                self.expr(0)
                self.state = 150
                self.match(AevumParser.T__1)
                self.state = 151
                self.statement_list()
                self.state = 152
                self.match(AevumParser.T__2)
                pass
            elif token in [9]:
                localctx = AevumParser.ParenthicalExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(AevumParser.T__8)
                self.state = 155
                self.expr(0)
                self.state = 156
                self.match(AevumParser.T__9)
                pass
            elif token in [6, 29, 30, 31, 32, 33]:
                localctx = AevumParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 188
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 186
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = AevumParser.MultplicationContext(self, AevumParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 161
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 162
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 163
                        self.expr(9)
                        pass

                    elif la_ == 2:
                        localctx = AevumParser.AdditionContext(self, AevumParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 164
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 165
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 166
                        self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = AevumParser.ComparisonContext(self, AevumParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 167
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 168
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 169
                        self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = AevumParser.AssignExprContext(self, AevumParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 170
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 171
                        self.match(AevumParser.T__13)
                        self.state = 172
                        self.expr(4)
                        pass

                    elif la_ == 5:
                        localctx = AevumParser.ArrayIndexContext(self, AevumParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 174
                        self.match(AevumParser.T__5)
                        self.state = 175
                        self.expr(0)
                        self.state = 176
                        self.match(AevumParser.T__6)
                        pass

                    elif la_ == 6:
                        localctx = AevumParser.FunctionCallContext(self, AevumParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 178
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 179
                        self.match(AevumParser.T__8)
                        self.state = 180
                        self.expr_list()
                        self.state = 181
                        self.match(AevumParser.T__9)
                        pass

                    elif la_ == 7:
                        localctx = AevumParser.MemberAccessContext(self, AevumParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 183
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 184
                        self.match(AevumParser.T__14)
                        self.state = 185
                        self.identifier()
                        pass

             
                self.state = 190
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(AevumParser.IdentifierContext,0)


        def boolean_literal(self):
            return self.getTypedRuleContext(AevumParser.Boolean_literalContext,0)


        def numeric_literal(self):
            return self.getTypedRuleContext(AevumParser.Numeric_literalContext,0)


        def string_literal(self):
            return self.getTypedRuleContext(AevumParser.String_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(AevumParser.Struct_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(AevumParser.Array_literalContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = AevumParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_atom)
        try:
            self.state = 197
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 192
                self.boolean_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 193
                self.numeric_literal()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 194
                self.string_literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 195
                self.struct_literal()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 196
                self.array_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(AevumParser.IDENT, 0)

        def getRuleIndex(self):
            return AevumParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = AevumParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(AevumParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AevumParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = AevumParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==29 or _la==30):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AevumParser.NUMBER, 0)

        def getRuleIndex(self):
            return AevumParser.RULE_numeric_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumeric_literal" ):
                return visitor.visitNumeric_literal(self)
            else:
                return visitor.visitChildren(self)




    def numeric_literal(self):

        localctx = AevumParser.Numeric_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_numeric_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(AevumParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AevumParser.STRING, 0)

        def getRuleIndex(self):
            return AevumParser.RULE_string_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_literal" ):
                return visitor.visitString_literal(self)
            else:
                return visitor.visitChildren(self)




    def string_literal(self):

        localctx = AevumParser.String_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(AevumParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(AevumParser.IdentifierContext,0)


        def field_initialiser_list(self):
            return self.getTypedRuleContext(AevumParser.Field_initialiser_listContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = AevumParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_struct_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.identifier()
            self.state = 208
            self.match(AevumParser.T__1)
            self.state = 209
            self.field_initialiser_list()
            self.state = 210
            self.match(AevumParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_initialiser_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_initialiser(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AevumParser.Field_initialiserContext)
            else:
                return self.getTypedRuleContext(AevumParser.Field_initialiserContext,i)


        def getRuleIndex(self):
            return AevumParser.RULE_field_initialiser_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_initialiser_list" ):
                return visitor.visitField_initialiser_list(self)
            else:
                return visitor.visitChildren(self)




    def field_initialiser_list(self):

        localctx = AevumParser.Field_initialiser_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_field_initialiser_list)
        self._la = 0 # Token type
        try:
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 212
                self.field_initialiser()
                self.state = 217
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 213
                        self.match(AevumParser.T__3)
                        self.state = 214
                        self.field_initialiser() 
                    self.state = 219
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 220
                    self.match(AevumParser.T__3)


                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_initialiserContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(AevumParser.IdentifierContext,0)


        def expr(self):
            return self.getTypedRuleContext(AevumParser.ExprContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_field_initialiser

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_initialiser" ):
                return visitor.visitField_initialiser(self)
            else:
                return visitor.visitChildren(self)




    def field_initialiser(self):

        localctx = AevumParser.Field_initialiserContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_field_initialiser)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.identifier()
            self.state = 227
            self.match(AevumParser.T__4)
            self.state = 228
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_list(self):
            return self.getTypedRuleContext(AevumParser.Expr_listContext,0)


        def getRuleIndex(self):
            return AevumParser.RULE_array_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




    def array_literal(self):

        localctx = AevumParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_array_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(AevumParser.T__5)
            self.state = 231
            self.expr_list()
            self.state = 232
            self.match(AevumParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 9)
         




