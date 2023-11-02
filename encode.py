from dataclasses import dataclass, field
from symbols import SymbolTable
from abstract_syntax_tree import *
from llvmlite import ir

from typenames import ArrayType, BasicType, FunctionType, StructType, i32, i8, void

i8_type = ir.IntType(8)
i32_type = ir.IntType(32)

char_type = i8_type
ptr_size_type = i32_type


# Encodes an AST into WAT assembly
class Encoder:
    def __init__(self, module: ir.Module, symbols: SymbolTable):
        self.module = module
        self.symbols = symbols
        self.next_constant = 0
        self.types: dict[str | BasicType] = {
            None: void,
            "i32": i32,
            "str": ArrayType(i8),
        }

    def visit_ast(self, ast: list[Function]):
        for declaration in ast:
            if isinstance(declaration, Struct):
                self.visit_struct(declaration)
            if isinstance(declaration, Function):
                self.visit_function(declaration)

    def visit_struct(self, s: Struct):
        self.symbols.define(s.name, s)

        self.types[s.name] = s.typeclass

    def visit_function(self, f: Function):
        self.symbols.define(f.name, f)
        self.symbols.push_scope()
        
        func = ir.Function(self.module, f.typeclass.llvm_type, name=f.name)
        f.llvm_value = func

        for a, arg in zip(f.args, func.args):
            arg.name = a.name
            a.llvm_value = arg
            self.symbols.define(a.name, a)

        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        last: Any = None
        for s in f.statements:
            if isinstance(s, Let):
                self.visit_let(s, builder)
            else:
                last = self.visit_expr(s, builder)

        if last and last.type != ir.VoidType():
            builder.ret(last)
        else:
            builder.ret_void()

        self.symbols.pop_scope()

    def visit_let(self, s: Let, builder: ir.IRBuilder):
        s.llvm_value = self.visit_expr(s.value, builder)
        s.typeclass = s.value.typeclass
        self.symbols.define(s.name, s)

    def visit_expr(self, s, builder: ir.IRBuilder):
        if isinstance(s, FunctionCall):
            f = self.symbols.lookup(s.name.value)
            args = [self.visit_expr(a, builder) for a in s.args]
            return builder.call(f.llvm_value, args)
        if isinstance(s, Operator):
            left = self.visit_expr(s.left, builder)
            right = self.visit_expr(s.right, builder)
            if s.op == '+':
                return builder.add(left.llvm_value, right.llvm_value)
            if s.op == '-':
                return builder.sub(left.llvm_value, right.llvm_value)
            if s.op == '*':
                return builder.mul(left.llvm_value, right.llvm_value)
            if s.op == '/':
                return builder.udiv(left.llvm_value, right.llvm_value)
        if isinstance(s, MemberAccess):
            source = self.visit_expr(s.source, builder)
            s.typeclass = s.source.typeclass
            pointer: ir.GEPInstr = builder.gep(
                source.llvm_value, [ir.Constant(i32_type, 0), ir.Constant(i32_type, 0)]
            )
            # print(pointer)
            return builder.load(pointer)
        if isinstance(s, Ident):
            t = self.symbols.lookup(s.value)
            return t
        if isinstance(s, NumericLiteral):
            return ir.Constant(i32_type, int(s.value))
        if isinstance(s, StringLiteral):
            encoded = bytearray(s.value.encode())
            l = len(encoded)

            t = ir.ArrayType(char_type, l)
            g = ir.GlobalVariable(
                self.module, t, self.module.get_unique_name("string_literal")
            )
            g.initializer = t(encoded)
            self.next_constant += 1

            return ir.Constant.literal_struct(
                [
                    ir.Constant(ptr_size_type, l),
                    g.bitcast(ir.PointerType(char_type)),
                ]
            )
        if isinstance(s, StructLiteral):
            t: Struct = self.symbols.lookup(s.name)
            storage = builder.alloca(t.typeclass.llvm_type)
            literal = ir.Constant(t.typeclass.llvm_type, ir.Undefined)
            initialisers = {
                m.name: self.visit_expr(m.value, builder) for m in s.members
            }
            for i, m in enumerate(t.members):
                if m.name in initialisers:
                    literal = builder.insert_value(
                        literal, initialisers[m.name], i
                    )
            builder.store(literal, storage)
            return storage

    def __repr__(self):
        return str(self.module)

