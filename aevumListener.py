# Generated from aevum.g4 by ANTLR 4.5.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .aevumParser import aevumParser
else:
    from aevumParser import aevumParser

# This class defines a complete listener for a parse tree produced by aevumParser.
class aevumListener(ParseTreeListener):

    # Enter a parse tree produced by aevumParser#top_level.
    def enterTop_level(self, ctx:aevumParser.Top_levelContext):
        pass

    # Exit a parse tree produced by aevumParser#top_level.
    def exitTop_level(self, ctx:aevumParser.Top_levelContext):
        pass


    # Enter a parse tree produced by aevumParser#struct_def.
    def enterStruct_def(self, ctx:aevumParser.Struct_defContext):
        pass

    # Exit a parse tree produced by aevumParser#struct_def.
    def exitStruct_def(self, ctx:aevumParser.Struct_defContext):
        pass


    # Enter a parse tree produced by aevumParser#struct_body.
    def enterStruct_body(self, ctx:aevumParser.Struct_bodyContext):
        pass

    # Exit a parse tree produced by aevumParser#struct_body.
    def exitStruct_body(self, ctx:aevumParser.Struct_bodyContext):
        pass


    # Enter a parse tree produced by aevumParser#var_decl.
    def enterVar_decl(self, ctx:aevumParser.Var_declContext):
        pass

    # Exit a parse tree produced by aevumParser#var_decl.
    def exitVar_decl(self, ctx:aevumParser.Var_declContext):
        pass


    # Enter a parse tree produced by aevumParser#type_expr.
    def enterType_expr(self, ctx:aevumParser.Type_exprContext):
        pass

    # Exit a parse tree produced by aevumParser#type_expr.
    def exitType_expr(self, ctx:aevumParser.Type_exprContext):
        pass


    # Enter a parse tree produced by aevumParser#cdecl.
    def enterCdecl(self, ctx:aevumParser.CdeclContext):
        pass

    # Exit a parse tree produced by aevumParser#cdecl.
    def exitCdecl(self, ctx:aevumParser.CdeclContext):
        pass


    # Enter a parse tree produced by aevumParser#function_def.
    def enterFunction_def(self, ctx:aevumParser.Function_defContext):
        pass

    # Exit a parse tree produced by aevumParser#function_def.
    def exitFunction_def(self, ctx:aevumParser.Function_defContext):
        pass


    # Enter a parse tree produced by aevumParser#function_decl.
    def enterFunction_decl(self, ctx:aevumParser.Function_declContext):
        pass

    # Exit a parse tree produced by aevumParser#function_decl.
    def exitFunction_decl(self, ctx:aevumParser.Function_declContext):
        pass


    # Enter a parse tree produced by aevumParser#function_args.
    def enterFunction_args(self, ctx:aevumParser.Function_argsContext):
        pass

    # Exit a parse tree produced by aevumParser#function_args.
    def exitFunction_args(self, ctx:aevumParser.Function_argsContext):
        pass


    # Enter a parse tree produced by aevumParser#function_arg_list.
    def enterFunction_arg_list(self, ctx:aevumParser.Function_arg_listContext):
        pass

    # Exit a parse tree produced by aevumParser#function_arg_list.
    def exitFunction_arg_list(self, ctx:aevumParser.Function_arg_listContext):
        pass


    # Enter a parse tree produced by aevumParser#block.
    def enterBlock(self, ctx:aevumParser.BlockContext):
        pass

    # Exit a parse tree produced by aevumParser#block.
    def exitBlock(self, ctx:aevumParser.BlockContext):
        pass


    # Enter a parse tree produced by aevumParser#statement.
    def enterStatement(self, ctx:aevumParser.StatementContext):
        pass

    # Exit a parse tree produced by aevumParser#statement.
    def exitStatement(self, ctx:aevumParser.StatementContext):
        pass


    # Enter a parse tree produced by aevumParser#let_var.
    def enterLet_var(self, ctx:aevumParser.Let_varContext):
        pass

    # Exit a parse tree produced by aevumParser#let_var.
    def exitLet_var(self, ctx:aevumParser.Let_varContext):
        pass


    # Enter a parse tree produced by aevumParser#assignment.
    def enterAssignment(self, ctx:aevumParser.AssignmentContext):
        pass

    # Exit a parse tree produced by aevumParser#assignment.
    def exitAssignment(self, ctx:aevumParser.AssignmentContext):
        pass


    # Enter a parse tree produced by aevumParser#expression_list.
    def enterExpression_list(self, ctx:aevumParser.Expression_listContext):
        pass

    # Exit a parse tree produced by aevumParser#expression_list.
    def exitExpression_list(self, ctx:aevumParser.Expression_listContext):
        pass


    # Enter a parse tree produced by aevumParser#expression.
    def enterExpression(self, ctx:aevumParser.ExpressionContext):
        pass

    # Exit a parse tree produced by aevumParser#expression.
    def exitExpression(self, ctx:aevumParser.ExpressionContext):
        pass


    # Enter a parse tree produced by aevumParser#call_expression.
    def enterCall_expression(self, ctx:aevumParser.Call_expressionContext):
        pass

    # Exit a parse tree produced by aevumParser#call_expression.
    def exitCall_expression(self, ctx:aevumParser.Call_expressionContext):
        pass


    # Enter a parse tree produced by aevumParser#dummy_member_expression.
    def enterDummy_member_expression(self, ctx:aevumParser.Dummy_member_expressionContext):
        pass

    # Exit a parse tree produced by aevumParser#dummy_member_expression.
    def exitDummy_member_expression(self, ctx:aevumParser.Dummy_member_expressionContext):
        pass


    # Enter a parse tree produced by aevumParser#member_expression.
    def enterMember_expression(self, ctx:aevumParser.Member_expressionContext):
        pass

    # Exit a parse tree produced by aevumParser#member_expression.
    def exitMember_expression(self, ctx:aevumParser.Member_expressionContext):
        pass


    # Enter a parse tree produced by aevumParser#atom.
    def enterAtom(self, ctx:aevumParser.AtomContext):
        pass

    # Exit a parse tree produced by aevumParser#atom.
    def exitAtom(self, ctx:aevumParser.AtomContext):
        pass


    # Enter a parse tree produced by aevumParser#named_reference.
    def enterNamed_reference(self, ctx:aevumParser.Named_referenceContext):
        pass

    # Exit a parse tree produced by aevumParser#named_reference.
    def exitNamed_reference(self, ctx:aevumParser.Named_referenceContext):
        pass


    # Enter a parse tree produced by aevumParser#literal.
    def enterLiteral(self, ctx:aevumParser.LiteralContext):
        pass

    # Exit a parse tree produced by aevumParser#literal.
    def exitLiteral(self, ctx:aevumParser.LiteralContext):
        pass


    # Enter a parse tree produced by aevumParser#floating_point_literal.
    def enterFloating_point_literal(self, ctx:aevumParser.Floating_point_literalContext):
        pass

    # Exit a parse tree produced by aevumParser#floating_point_literal.
    def exitFloating_point_literal(self, ctx:aevumParser.Floating_point_literalContext):
        pass


    # Enter a parse tree produced by aevumParser#string_literal.
    def enterString_literal(self, ctx:aevumParser.String_literalContext):
        pass

    # Exit a parse tree produced by aevumParser#string_literal.
    def exitString_literal(self, ctx:aevumParser.String_literalContext):
        pass


    # Enter a parse tree produced by aevumParser#integer_literal.
    def enterInteger_literal(self, ctx:aevumParser.Integer_literalContext):
        pass

    # Exit a parse tree produced by aevumParser#integer_literal.
    def exitInteger_literal(self, ctx:aevumParser.Integer_literalContext):
        pass


