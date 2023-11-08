from dataclasses import dataclass
from typing import Any
from abstract_syntax_tree import Assignment, BooleanLiteral, Comparison, Function, FunctionCall, Ident, IfElse, Let, MemberAccess, Node, NumericLiteral, Operator, StringLiteral, Struct, StructLiteral, Variable
from symbols import SymbolTable
from llvmlite import ir

from typenames import ArrayType, BasicType, FunctionType, StructType, i32, i8, void, boolean, char_type, ptr_size_type


class Value:
    def load(self, _builder: ir.IRBuilder):
        pass  # override in subclass


@dataclass
class Temporary(Value):
    data: ir.Value

    def load(self, _builder: ir.IRBuilder):
        return self.data


@dataclass
class Stored(Temporary):
    def load(self, builder: ir.IRBuilder):
        return builder.load(self.data)

# Encodes an AST into LLVM IR


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
            if arg.type.is_pointer:
                a.llvm_value = Stored(arg)
            else:
                a.llvm_value = Temporary(arg)
            self.visit_variable(a)

        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        last: Any = None
        for s in f.statements:
            last = self.visit_statement(s, builder)

        if last and last.data.type != ir.VoidType():
            builder.ret(last.load(builder))
        else:
            builder.ret_void()

        self.symbols.pop_scope()

    def visit_statement(self, s: Node, builder: ir.IRBuilder):
        if isinstance(s, Let):
            return self.visit_let(s, builder)
        else:
            return self.visit_expr(s, builder)

    def visit_variable(self, s: Variable):
        self.symbols.define(s.name, s)

    def visit_let(self, s: Let, builder: ir.IRBuilder):
        self.visit_variable(s.variable)
        value = self.visit_expr(s.value, builder)
        storage = builder.alloca(
            s.variable.typeclass.llvm_type, name=s.variable.name)
        builder.store(value.load(builder), storage)
        s.variable.llvm_value = Stored(storage)

    def visit_expr(self, s, builder: ir.IRBuilder) -> Value | None:
        if isinstance(s, FunctionCall):
            f = self.symbols.lookup(s.name.value)
            args = [self.visit_expr(a, builder) for a in s.args]
            args = [a.load(builder) for a in args]
            result = builder.call(f.llvm_value, args)
            if result.type.is_pointer:
                return Stored(result)
            else:
                return Temporary(result)
        if isinstance(s, Operator):
            left = self.visit_expr(s.left, builder).load(builder)
            right = self.visit_expr(s.right, builder).load(builder)
            if s.op == '+':
                return Temporary(builder.add(left, right))
            if s.op == '-':
                return Temporary(builder.sub(left, right))
            if s.op == '*':
                return Temporary(builder.mul(left, right))
            if s.op == '/':
                return Temporary(builder.udiv(left, right))
            raise Exception(f"unknown operator {s.op}")
        if isinstance(s, Comparison):
            left = self.visit_expr(s.left, builder).load(builder)
            right = self.visit_expr(s.right, builder).load(builder)
            return Temporary(builder.icmp_signed(s.op, left, right))
        if isinstance(s, IfElse):
            condition = self.visit_expr(s.condition, builder).load(builder)
            then_block = None
            else_block = None
            with builder.if_else(condition) as (then, otherwise):
                with then:
                    for t in s.then_statements:
                        last_then = self.visit_statement(t, builder)
                    then_block = builder.block
                with otherwise:
                    for t in s.else_statements:
                        last_else = self.visit_statement(t, builder)
                    else_block = builder.block

            if s.typeclass != void:
                phi = builder.phi(s.then_statements[-1].typeclass.llvm_type)
                if then_block:
                    phi.add_incoming(last_then.load(builder), then_block)
                if else_block:
                    phi.add_incoming(last_else.load(builder), else_block)
                if phi.type.is_pointer:
                    return Stored(phi)
                else:
                    return Temporary(phi)
        if isinstance(s, Assignment):
            target = self.visit_expr(s.left, builder)
            value = self.visit_expr(s.right, builder)
            builder.store(value.load(builder), target.data)
            return value
        if isinstance(s, MemberAccess):
            source = self.visit_expr(s.source, builder)
            field_index = s.source.typeclass.member_names[s.field]
            pointer: ir.GEPInstr = builder.gep(
                source.data, [ir.Constant(i32.llvm_type, 0), ir.Constant(
                    i32.llvm_type, field_index)]
            )
            return Stored(pointer)
        if isinstance(s, Ident):
            t = self.symbols.lookup(s.value)
            return t.llvm_value
        if isinstance(s, BooleanLiteral):
            return Temporary(ir.Constant(boolean.llvm_type, int(s.value)))
        if isinstance(s, NumericLiteral):
            return Temporary(ir.Constant(i32.llvm_type, int(s.value)))
        if isinstance(s, StringLiteral):
            encoded = bytearray(s.value.encode())
            l = len(encoded)

            t = ir.ArrayType(char_type.llvm_type, l)
            g = ir.GlobalVariable(
                self.module, t, self.module.get_unique_name("string_literal")
            )
            g.initializer = t(encoded)
            self.next_constant += 1

            storage = builder.alloca(ArrayType(i8).llvm_type)
            builder.store(ir.Constant.literal_struct(
                [
                    ir.Constant(ptr_size_type.llvm_type, l),
                    g.bitcast(ir.PointerType(char_type.llvm_type)),
                ]
            ), storage)
            return Stored(storage)
        if isinstance(s, StructLiteral):
            t: Struct = self.symbols.lookup(s.name)
            storage = builder.alloca(t.typeclass.llvm_type)
            literal = ir.Constant(t.typeclass.llvm_type, ir.Undefined)
            initialisers = {
                m.name: self.visit_expr(m.value, builder) for m in s.members
            }
            for i, m in enumerate(t.members):
                if m.name in initialisers:
                    value = initialisers[m.name].load(builder)
                    literal = builder.insert_value(
                        literal, value, i
                    )
            builder.store(literal, storage)
            return Stored(storage)
        # raise Exception(f"unknown exxpression {s}")

    def __repr__(self):
        return str(self.module)
