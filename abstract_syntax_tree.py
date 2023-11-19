from dataclasses import dataclass
from AevumParser import AevumParser
from AevumVisitor import AevumVisitor
from typing import Any, Optional
from llvmlite import ir

from typenames import BasicType


@dataclass(kw_only=True)
class Node:
    typeclass: Optional[BasicType] = None


@dataclass
class Ident(Node):
    value: str


@dataclass
class BooleanLiteral(Node):
    value: bool


@dataclass
class NumericLiteral(Node):
    value: str


@dataclass
class StringLiteral(Node):
    value: str


@dataclass
class Operator(Node):
    op: str
    left: Node
    right: Node


@dataclass
class Comparison(Node):
    op: str
    left: Node
    right: Node


@dataclass
class IfElse(Node):
    condition: Node
    then_statements: list[Node]
    else_statements: list[Node]


@dataclass
class WhileLoop(Node):
    condition: Node
    statements: list[Node]


@dataclass
class Assignment(Node):
    left: Node
    right: Node


@dataclass
class Variable(Node):
    name: str
    typename: str
    llvm_value: Optional[Any] = None


@dataclass
class Struct(Node):
    name: str
    members: list[Variable]


@dataclass
class Function(Node):
    name: str
    args: list[Variable]
    return_type: str
    statements: list
    llvm_value: Optional[Any] = None


@dataclass
class Let(Node):
    variable: Variable
    value: Node
    llvm_value: Optional[Any] = None


@dataclass
class FieldInitialiser(Node):
    name: str
    value: Node


@dataclass
class StructLiteral(Node):
    name: str
    members: list[FieldInitialiser]


@dataclass
class FunctionCall(Node):
    name: str
    args: list


@dataclass
class MemberAccess(Node):
    source: Node
    field: str


# walks the parse tree and converts it to an AST
class ASTGenerator(AevumVisitor):
    def visitModule(self, ctx: AevumParser.ModuleContext):
        return [self.visit(c) for c in ctx.children[0:-1]]

    def visitDeclaration(self, ctx: AevumParser.DeclarationContext):
        return self.visit(ctx.children[0])

    def visitStruct(self, ctx: AevumParser.StructContext):
        name = self.visit(ctx.children[1]).value
        members = self.visit(ctx.children[3])
        return Struct(name, members)

    def visitVariable_list(self, ctx: AevumParser.Variable_listContext):
        return [self.visit(c) for i, c in enumerate(ctx.children or []) if i % 2 == 0]

    def visitVariable(self, ctx: AevumParser.VariableContext):
        return Variable(
            self.visit(ctx.children[0]).value, self.visit(
                ctx.children[2]).value
        )

    def visitFunction(self, ctx: AevumParser.FunctionContext):
        name = self.visit(ctx.children[1]).value
        args = self.visit(ctx.children[3])
        return_type = self.visit(ctx.children[5])
        statements = self.visit(ctx.children[7])
        f = Function(
            name, args, return_type.value if return_type else None, statements)
        # print(f)
        return f

    def visitBasicType(self, ctx: AevumParser.BasicTypeContext):
        return self.visit(ctx.children[0])

    def visitReturn_type(self, ctx: AevumParser.Return_typeContext):
        if ctx.children:
            return self.visit(ctx.children[1])

    def visitStatement_list(self, ctx: AevumParser.Statement_listContext):
        children = ctx.children
        if not children:
            return []
        first = self.visit(children.pop(0))
        if len(children) == 0:
            return [first]
        next = children.pop(0)
        if next.getText() == ';':
            next = children.pop(0)
        return [first] + self.visit(next)

    def visitTerminated_statement(self, ctx:AevumParser.Terminated_statementContext):
        return self.visit(ctx.children[0])

    def visitLetStatement(self, ctx: AevumParser.LetStatementContext):
        variable = self.visit(ctx.children[1])
        expr = self.visit(ctx.children[3])
        return Let(variable, expr)

    def visitExprStatement(self, ctx: AevumParser.ExprStatementContext):
        return self.visit(ctx.children[0])

    def visitExpr_list(self, ctx: AevumParser.Expr_listContext):
        return [self.visit(c) for i, c in enumerate(ctx.children or []) if i % 2 == 0]

    def visitTerminatedExpr(self, ctx:AevumParser.TerminatedExprContext):
        return self.visit(ctx.children[0])

    def visitFunctionCall(self, ctx: AevumParser.FunctionCallContext):
        return FunctionCall(
            self.visit(ctx.children[0]), self.visit(ctx.children[2]) or []
        )

    def visitMemberAccess(self, ctx: AevumParser.MemberAccessContext):
        source = self.visit(ctx.children[0])
        field = self.visit(ctx.children[2]).value
        return MemberAccess(source, field)

    def visitAddition(self, ctx: AevumParser.AdditionContext):
        return Operator(
            self.visit(ctx.children[1]),
            self.visit(ctx.children[0]),
            self.visit(ctx.children[2]),
        )

    def visitComparison(self, ctx: AevumParser.ComparisonContext):
        return Comparison(self.visit(ctx.children[1]), self.visit(ctx.children[0]), self.visit(ctx.children[2]))

    def visitIfElse(self, ctx: AevumParser.IfElseContext):
        return IfElse(self.visit(ctx.children[1]), self.visit(ctx.children[3]), self.visit(ctx.children[7]) if len(ctx.children) > 7 else list())

    def visitWhileLoop(self, ctx: AevumParser.WhileLoopContext):
        return WhileLoop(self.visit(ctx.children[1]), self.visit(ctx.children[3]))

    def visitAssignExpr(self, ctx: AevumParser.AssignExprContext):
        return Assignment(self.visit(ctx.children[0]), self.visit(ctx.children[2]))

    def visitParenthicalExpr(self, ctx: AevumParser.ParenthicalExprContext):
        return self.visit(ctx.children[1])

    def visitAtomExpr(self, ctx: AevumParser.AtomExprContext):
        return self.visit(ctx.children[0])

    def visitAtom(self, ctx: AevumParser.AtomContext):
        return self.visit(ctx.children[0])

    def visitString_literal(self, ctx: AevumParser.String_literalContext):
        return StringLiteral(ctx.getText()[1:-1])

    def visitStruct_literal(self, ctx: AevumParser.Struct_literalContext):
        name = self.visit(ctx.children[0]).value
        members = self.visit(ctx.children[2])
        return StructLiteral(name, members)

    def visitField_initialiser_list(
        self, ctx: AevumParser.Field_initialiser_listContext
    ):
        return [self.visit(c) for i, c in enumerate(ctx.children or []) if i % 2 == 0]

    def visitField_initialiser(self, ctx: AevumParser.Field_initialiserContext):
        name = self.visit(ctx.children[0]).value
        value = self.visit(ctx.children[2])
        return FieldInitialiser(name, value)

    def visitIdentifier(self, ctx: AevumParser.IdentifierContext):
        return Ident(ctx.getText())

    def visitBoolean_literal(self, ctx: AevumParser.Boolean_literalContext):
        return BooleanLiteral(ctx.getText() == 'true')

    def visitNumeric_literal(self, ctx: AevumParser.Numeric_literalContext):
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
