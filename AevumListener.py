# Generated from .\Aevum.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .AevumParser import AevumParser
else:
    from AevumParser import AevumParser

# This class defines a complete listener for a parse tree produced by AevumParser.
class AevumListener(ParseTreeListener):

    # Enter a parse tree produced by AevumParser#module.
    def enterModule(self, ctx:AevumParser.ModuleContext):
        pass

    # Exit a parse tree produced by AevumParser#module.
    def exitModule(self, ctx:AevumParser.ModuleContext):
        pass


    # Enter a parse tree produced by AevumParser#declaration.
    def enterDeclaration(self, ctx:AevumParser.DeclarationContext):
        pass

    # Exit a parse tree produced by AevumParser#declaration.
    def exitDeclaration(self, ctx:AevumParser.DeclarationContext):
        pass


    # Enter a parse tree produced by AevumParser#struct.
    def enterStruct(self, ctx:AevumParser.StructContext):
        pass

    # Exit a parse tree produced by AevumParser#struct.
    def exitStruct(self, ctx:AevumParser.StructContext):
        pass


    # Enter a parse tree produced by AevumParser#field_list.
    def enterField_list(self, ctx:AevumParser.Field_listContext):
        pass

    # Exit a parse tree produced by AevumParser#field_list.
    def exitField_list(self, ctx:AevumParser.Field_listContext):
        pass


    # Enter a parse tree produced by AevumParser#field.
    def enterField(self, ctx:AevumParser.FieldContext):
        pass

    # Exit a parse tree produced by AevumParser#field.
    def exitField(self, ctx:AevumParser.FieldContext):
        pass


    # Enter a parse tree produced by AevumParser#BasicType.
    def enterBasicType(self, ctx:AevumParser.BasicTypeContext):
        pass

    # Exit a parse tree produced by AevumParser#BasicType.
    def exitBasicType(self, ctx:AevumParser.BasicTypeContext):
        pass


    # Enter a parse tree produced by AevumParser#ArrayType.
    def enterArrayType(self, ctx:AevumParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by AevumParser#ArrayType.
    def exitArrayType(self, ctx:AevumParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by AevumParser#function.
    def enterFunction(self, ctx:AevumParser.FunctionContext):
        pass

    # Exit a parse tree produced by AevumParser#function.
    def exitFunction(self, ctx:AevumParser.FunctionContext):
        pass


    # Enter a parse tree produced by AevumParser#arg_list.
    def enterArg_list(self, ctx:AevumParser.Arg_listContext):
        pass

    # Exit a parse tree produced by AevumParser#arg_list.
    def exitArg_list(self, ctx:AevumParser.Arg_listContext):
        pass


    # Enter a parse tree produced by AevumParser#arg.
    def enterArg(self, ctx:AevumParser.ArgContext):
        pass

    # Exit a parse tree produced by AevumParser#arg.
    def exitArg(self, ctx:AevumParser.ArgContext):
        pass


    # Enter a parse tree produced by AevumParser#return_type.
    def enterReturn_type(self, ctx:AevumParser.Return_typeContext):
        pass

    # Exit a parse tree produced by AevumParser#return_type.
    def exitReturn_type(self, ctx:AevumParser.Return_typeContext):
        pass


    # Enter a parse tree produced by AevumParser#statement_list.
    def enterStatement_list(self, ctx:AevumParser.Statement_listContext):
        pass

    # Exit a parse tree produced by AevumParser#statement_list.
    def exitStatement_list(self, ctx:AevumParser.Statement_listContext):
        pass


    # Enter a parse tree produced by AevumParser#LetStatement.
    def enterLetStatement(self, ctx:AevumParser.LetStatementContext):
        pass

    # Exit a parse tree produced by AevumParser#LetStatement.
    def exitLetStatement(self, ctx:AevumParser.LetStatementContext):
        pass


    # Enter a parse tree produced by AevumParser#ExprStatement.
    def enterExprStatement(self, ctx:AevumParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by AevumParser#ExprStatement.
    def exitExprStatement(self, ctx:AevumParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by AevumParser#expr_list.
    def enterExpr_list(self, ctx:AevumParser.Expr_listContext):
        pass

    # Exit a parse tree produced by AevumParser#expr_list.
    def exitExpr_list(self, ctx:AevumParser.Expr_listContext):
        pass


    # Enter a parse tree produced by AevumParser#Addition.
    def enterAddition(self, ctx:AevumParser.AdditionContext):
        pass

    # Exit a parse tree produced by AevumParser#Addition.
    def exitAddition(self, ctx:AevumParser.AdditionContext):
        pass


    # Enter a parse tree produced by AevumParser#MemberAccess.
    def enterMemberAccess(self, ctx:AevumParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by AevumParser#MemberAccess.
    def exitMemberAccess(self, ctx:AevumParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by AevumParser#Multplication.
    def enterMultplication(self, ctx:AevumParser.MultplicationContext):
        pass

    # Exit a parse tree produced by AevumParser#Multplication.
    def exitMultplication(self, ctx:AevumParser.MultplicationContext):
        pass


    # Enter a parse tree produced by AevumParser#FunctionCall.
    def enterFunctionCall(self, ctx:AevumParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by AevumParser#FunctionCall.
    def exitFunctionCall(self, ctx:AevumParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by AevumParser#AtomExpr.
    def enterAtomExpr(self, ctx:AevumParser.AtomExprContext):
        pass

    # Exit a parse tree produced by AevumParser#AtomExpr.
    def exitAtomExpr(self, ctx:AevumParser.AtomExprContext):
        pass


    # Enter a parse tree produced by AevumParser#ArrayIndex.
    def enterArrayIndex(self, ctx:AevumParser.ArrayIndexContext):
        pass

    # Exit a parse tree produced by AevumParser#ArrayIndex.
    def exitArrayIndex(self, ctx:AevumParser.ArrayIndexContext):
        pass


    # Enter a parse tree produced by AevumParser#atom.
    def enterAtom(self, ctx:AevumParser.AtomContext):
        pass

    # Exit a parse tree produced by AevumParser#atom.
    def exitAtom(self, ctx:AevumParser.AtomContext):
        pass


    # Enter a parse tree produced by AevumParser#identifier.
    def enterIdentifier(self, ctx:AevumParser.IdentifierContext):
        pass

    # Exit a parse tree produced by AevumParser#identifier.
    def exitIdentifier(self, ctx:AevumParser.IdentifierContext):
        pass


    # Enter a parse tree produced by AevumParser#number.
    def enterNumber(self, ctx:AevumParser.NumberContext):
        pass

    # Exit a parse tree produced by AevumParser#number.
    def exitNumber(self, ctx:AevumParser.NumberContext):
        pass


    # Enter a parse tree produced by AevumParser#string_literal.
    def enterString_literal(self, ctx:AevumParser.String_literalContext):
        pass

    # Exit a parse tree produced by AevumParser#string_literal.
    def exitString_literal(self, ctx:AevumParser.String_literalContext):
        pass


    # Enter a parse tree produced by AevumParser#struct_literal.
    def enterStruct_literal(self, ctx:AevumParser.Struct_literalContext):
        pass

    # Exit a parse tree produced by AevumParser#struct_literal.
    def exitStruct_literal(self, ctx:AevumParser.Struct_literalContext):
        pass


    # Enter a parse tree produced by AevumParser#field_initialiser_list.
    def enterField_initialiser_list(self, ctx:AevumParser.Field_initialiser_listContext):
        pass

    # Exit a parse tree produced by AevumParser#field_initialiser_list.
    def exitField_initialiser_list(self, ctx:AevumParser.Field_initialiser_listContext):
        pass


    # Enter a parse tree produced by AevumParser#field_initialiser.
    def enterField_initialiser(self, ctx:AevumParser.Field_initialiserContext):
        pass

    # Exit a parse tree produced by AevumParser#field_initialiser.
    def exitField_initialiser(self, ctx:AevumParser.Field_initialiserContext):
        pass


    # Enter a parse tree produced by AevumParser#array_literal.
    def enterArray_literal(self, ctx:AevumParser.Array_literalContext):
        pass

    # Exit a parse tree produced by AevumParser#array_literal.
    def exitArray_literal(self, ctx:AevumParser.Array_literalContext):
        pass



del AevumParser