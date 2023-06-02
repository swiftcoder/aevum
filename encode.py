from dataclasses import dataclass, field
from typing import Any
from antlr4 import *
from AevumParser import AevumParser
from AevumVisitor import AevumVisitor


@dataclass
class Ident:
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


@dataclass
class FunctionCall:
    name: str
    args: list


class SymbolTable:
    def __init__(self):
        self.table = [dict()]

    def push_scope(self):
        self.table.append(dict())

    def pop_scope(self):
        if len(self.table) < 2:
            raise Exception("attempted to pop the global scope")
        self.table.pop()

    def define(self, name, value):
        self.table[-1][name] = value

    def lookup(self, name):
        print(f"looking up {name}")
        for i in range(len(self.table) - 1, -1, -1):
            if name in self.table[i]:
                return self.table[i][name]


class Encoder:
    def __init__(self, symbols: SymbolTable):
        self.symbols = symbols
        self.constants = []
        self.constant_offset = 0
        self.functions = []

    def encode_function(self, f: Function):
        self.symbols.define(f.name, f)
        self.symbols.push_scope()

        for a in f.args:
            self.symbols.define(a.name, a)

        args = " ".join([f"(param ${a.name} {a.typename})" for a in f.args])
        result = f"(result {f.return_type})" if f.return_type else ""
        body = "\n".join([self.encode_statement(s) for s in f.statements])
        self.functions.append(f"(func ${f.name} {args} {result}\n{body})")

        self.symbols.pop_scope()

    def encode_statement(self, s):
        return self.encode_expr(s, 1)

    def encode_expr(self, s, indent: int):
        tabs = "\t" * indent
        if isinstance(s, FunctionCall):
            f = self.symbols.lookup(s.name.value)
            args = "\n".join([self.encode_expr(a, indent) for a in s.args])
            return f"{args}\n{tabs}call ${f.name}"
        if isinstance(s, StringLiteral):
            offset = self.constant_offset
            length = len(s.value)
            self.constant_offset += length
            self.constants.append(s.value)
            return f'{tabs}i32.const {offset} ;; string "{s.value}"\n{tabs}i32.const {length}'
        if isinstance(s, Operator):
            left = self.encode_expr(s.left, indent)
            right = self.encode_expr(s.right, indent)
            return f"{left}\n{right}\n{tabs}i32.add"
        if isinstance(s, Ident):
            return self.encode_expr(self.symbols.lookup(s.value), indent)
        if isinstance(s, Argument):
            return f"{tabs}local.get ${s.name}"

    def push_constant(self, c: str):
        self.stack.append((self.constant_offset, len(c)))
        self.constant_offset += len(c)
        self.constants.append(c)

    def __repr__(self):
        data_section = []
        offset = 0
        for c in self.constants:
            data_section.append(f'(data (i32.const {offset}) "{c}")')
            offset += len(c)

        data = "\n\t".join(data_section)
        functions = "\n\n".join(self.functions)

        return f"""
(module
    (import "runtime" "memory" (memory 1))
    (import "" "println" (func $println (param i32) (param i32)))

{data}

{functions}

    (export "main" (func $main))
)
        """


class Visitor(AevumVisitor):
    def __init__(self, encoder: Encoder):
        self.encoder = encoder

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
        print(f)
        self.encoder.encode_function(f)
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

    def visitTerminal(self, node):
        return node.getText()

    def defaultResult(self):
        return []

    def aggregateResult(self, aggregate, nextResult):
        return aggregate + [nextResult]


def encode(tree: AevumParser.ModuleContext, parser: AevumParser):
    symbols = SymbolTable()
    symbols.define("println", Function("println", [], None, []))

    encoder = Encoder(symbols)
    visitor = Visitor(encoder)
    ast = visitor.visit(tree)
    print(ast)
    # print(tree.toStringTree(recog=parser))

    return str(encoder)
