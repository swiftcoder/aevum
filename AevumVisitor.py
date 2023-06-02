# Generated from .\Aevum.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .AevumParser import AevumParser
else:
    from AevumParser import AevumParser

# This class defines a complete generic visitor for a parse tree produced by AevumParser.

class AevumVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AevumParser#module.
    def visitModule(self, ctx:AevumParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#declaration.
    def visitDeclaration(self, ctx:AevumParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#struct.
    def visitStruct(self, ctx:AevumParser.StructContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#field_list.
    def visitField_list(self, ctx:AevumParser.Field_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#field.
    def visitField(self, ctx:AevumParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#BasicType.
    def visitBasicType(self, ctx:AevumParser.BasicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#ArrayType.
    def visitArrayType(self, ctx:AevumParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#function.
    def visitFunction(self, ctx:AevumParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#arg_list.
    def visitArg_list(self, ctx:AevumParser.Arg_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#arg.
    def visitArg(self, ctx:AevumParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#return_type.
    def visitReturn_type(self, ctx:AevumParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#statement_list.
    def visitStatement_list(self, ctx:AevumParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#LetStatement.
    def visitLetStatement(self, ctx:AevumParser.LetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#ExprStatement.
    def visitExprStatement(self, ctx:AevumParser.ExprStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#expr_list.
    def visitExpr_list(self, ctx:AevumParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#Addition.
    def visitAddition(self, ctx:AevumParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#MemberAccess.
    def visitMemberAccess(self, ctx:AevumParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#Multplication.
    def visitMultplication(self, ctx:AevumParser.MultplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#FunctionCall.
    def visitFunctionCall(self, ctx:AevumParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#AtomExpr.
    def visitAtomExpr(self, ctx:AevumParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#ArrayIndex.
    def visitArrayIndex(self, ctx:AevumParser.ArrayIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#atom.
    def visitAtom(self, ctx:AevumParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#identifier.
    def visitIdentifier(self, ctx:AevumParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#number.
    def visitNumber(self, ctx:AevumParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#string_literal.
    def visitString_literal(self, ctx:AevumParser.String_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#struct_literal.
    def visitStruct_literal(self, ctx:AevumParser.Struct_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#field_initialiser_list.
    def visitField_initialiser_list(self, ctx:AevumParser.Field_initialiser_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#field_initialiser.
    def visitField_initialiser(self, ctx:AevumParser.Field_initialiserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AevumParser#array_literal.
    def visitArray_literal(self, ctx:AevumParser.Array_literalContext):
        return self.visitChildren(ctx)



del AevumParser