from dataclasses import dataclass, field
from symbols import SymbolTable
from abstract_syntax_tree import *
from llvmlite import ir

i8_type = ir.IntType(8)
i32_type = ir.IntType(32)

char_type = i8_type
ptr_size_type = i32_type

# Encodes an AST into WAT assembly
class Encoder:
    def __init__(self, symbols: SymbolTable):
        self.symbols = symbols
        self.next_constant = 0
        self.types: dict[str | ir.Type] = {
            None: ir.VoidType(),
            "i32": i32_type,
            "str": ir.LiteralStructType(
                [ptr_size_type, ir.PointerType(char_type)]
            ),
        }
        self.functions = []

        self.module = ir.Module(name="__main__")

        self.symbols.define(
            "println",
            Function(
                "println",
                [Argument("arg0", "str")],
                None,
                [],
                ir.Function(
                    self.module,
                    ir.FunctionType(ir.VoidType(), [self.types["str"]]),
                    "println",
                ),
            ),
        )

    def encode_ast(self, ast: list[Function]):
        for f in ast:
            self.encode_function(f)

    def encode_function(self, f: Function):
        self.symbols.define(f.name, f)
        self.symbols.push_scope()

        args = [self.types[a.typename] for a in f.args]
        return_type = self.types[f.return_type]

        func_type = ir.FunctionType(return_type, args)
        func = ir.Function(self.module, func_type, name=f.name)
        f.func = func

        for a, arg in zip(f.args, func.args):
            arg.name = a.name
            self.symbols.define(a.name, arg)

        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        last = None
        for s in f.statements:
            last = self.encode_expr(s, builder)

        if last and last.type != ir.VoidType():
            builder.ret(last)
        else:
            builder.ret_void()

        self.functions.append(func)

        self.symbols.pop_scope()

    def encode_expr(self, s, builder: ir.IRBuilder):
        if isinstance(s, FunctionCall):
            f = self.symbols.lookup(s.name.value)
            args = [self.encode_expr(a, builder) for a in s.args]
            return builder.call(f.func, args)
        if isinstance(s, Operator):
            left = self.encode_expr(s.left, builder)
            right = self.encode_expr(s.right, builder)
            return builder.add(left, right)
        if isinstance(s, Ident):
            return self.symbols.lookup(s.value)
        if isinstance(s, NumericLiteral):
            return ir.Constant(i32_type, int(s.value))
        if isinstance(s, StringLiteral):
            encoded = bytearray(s.value.encode())
            l = len(encoded)

            t = ir.ArrayType(char_type, l)
            g = ir.GlobalVariable(self.module, t, f"constant_{self.next_constant}")
            g.initializer = t(encoded)
            self.next_constant += 1

            return ir.Constant.literal_struct(
                [
                    ir.Constant(ptr_size_type, l),
                    g.bitcast(ir.PointerType(char_type)),
                ]
            )

    def __repr__(self):
        return str(self.module)


def encode(ast):
    symbols = SymbolTable()

    encoder = Encoder(symbols)
    encoder.encode_ast(ast)

    return str(encoder)
