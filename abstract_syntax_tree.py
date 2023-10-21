from dataclasses import dataclass
from AevumParser import AevumParser
from AevumVisitor import AevumVisitor
from typing import Any, Optional
from llvmlite import ir


@dataclass
class Ident:
    value: str

@dataclass
class NumericLiteral:
    value: str

@dataclass
class StringLiteral:
    value: str


@dataclass
class Operator:
    op: str
    left: Any
    right: Any


@dataclass
class Argument:
    name: str
    typename: str


@dataclass
class Function:
    name: str
    args: list
    return_type: str
    statements: list
    func: Optional[ir.Type] = None


@dataclass
class FunctionCall:
    name: str
    args: list


# walks the parse tree and converts it to an AST
class ASTGenerator(AevumVisitor):
    def visitModule(self, ctx: AevumParser.ModuleContext):
        return [self.visit(c) for c in ctx.children[0:-1]]

    def visitDeclaration(self, ctx: AevumParser.DeclarationContext):
        return self.visit(ctx.children[0])

    def visitFunction(self, ctx: AevumParser.FunctionContext):
        name = self.visit(ctx.children[1]).value
        args = self.visit(ctx.children[3])
        return_type = self.visit(ctx.children[5])
        statements = self.visit(ctx.children[7])
        f = Function(name, args, return_type.value if return_type else None, statements)
        # print(f)
        return f

    def visitArg_list(self, ctx: AevumParser.Field_listContext):
        return [self.visit(c) for i, c in enumerate(ctx.children or []) if i % 2 == 0]

    def visitArg(self, ctx: AevumParser.FieldContext):
        return Argument(
            self.visit(ctx.children[0]).value, self.visit(ctx.children[2]).value
        )

    def visitBasicType(self, ctx: AevumParser.BasicTypeContext):
        return self.visit(ctx.children[0])

    def visitReturn_type(self, ctx: AevumParser.Return_typeContext):
        if ctx.children:
            return self.visit(ctx.children[1])

    def visitStatement_list(self, ctx: AevumParser.Statement_listContext):
        return [self.visit(c) for i, c in enumerate(ctx.children or []) if i % 2 == 0]

    def visitExprStatement(self, ctx: AevumParser.ExprStatementContext):
        return self.visit(ctx.children[0])

    def visitExpr_list(self, ctx: AevumParser.Expr_listContext):
        return [self.visit(c) for i, c in enumerate(ctx.children or []) if i % 2 == 0]

    def visitFunctionCall(self, ctx: AevumParser.FunctionCallContext):
        return FunctionCall(
            self.visit(ctx.children[0]), self.visit(ctx.children[2]) or []
        )

    def visitAddition(self, ctx: AevumParser.AdditionContext):
        return Operator(
            self.visit(ctx.children[1]),
            self.visit(ctx.children[0]),
            self.visit(ctx.children[2]),
        )

    def visitAtomExpr(self, ctx: AevumParser.AtomExprContext):
        return self.visit(ctx.children[0])

    def visitAtom(self, ctx: AevumParser.AtomContext):
        return self.visit(ctx.children[0])

    def visitString_literal(self, ctx: AevumParser.String_literalContext):
        return StringLiteral(ctx.getText()[1:-1])

    def visitIdentifier(self, ctx: AevumParser.IdentifierContext):
        return Ident(ctx.getText())

    def visitNumber(self, ctx:AevumParser.NumberContext):
        return NumericLiteral(ctx.getText())

    def visitTerminal(self, node):
        return node.getText()

    def defaultResult(self):
        return []

    def aggregateResult(self, aggregate, nextResult):
        return aggregate + [nextResult]


def build_ast(tree: AevumParser.ModuleContext):
    visitor = ASTGenerator()
    return visitor.visit(tree)
