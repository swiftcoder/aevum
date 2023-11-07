
from abstract_syntax_tree import Argument, BooleanLiteral, Comparison, Function, FunctionCall, Ident, IfElse, Let, MemberAccess, Node, NumericLiteral, Operator, StringLiteral, Struct, StructLiteral
from symbols import SymbolTable
from typenames import ArrayType, BasicType, StructType, void, i8, i32, FunctionType, boolean
from llvmlite import ir


class TypeChecker:
    def __init__(self, module: ir.Module, symbols: SymbolTable):
        self.module = module
        self.symbols = symbols
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

        member_names = dict()
        for (i, m) in enumerate(s.members):
            m.typeclass = self.types[m.typename]
            member_names[m.name] = i
        
        llvm_type = self.module.context.get_identified_type(s.name)
        llvm_type.set_body(*[m.typeclass.llvm_type for m in s.members])
        s.typeclass = StructType(
            name=s.name, members=s.members, member_names=member_names, llvm_type=llvm_type)

        self.types[s.name] = s.typeclass

    def visit_function(self, f: Function):
        self.symbols.define(f.name, f)
        self.symbols.push_scope()

        for a in f.args:
            a.typeclass = self.types[a.typename]
            self.symbols.define(a.name, a)

        args = [a.typeclass for a in f.args]
        return_type = self.types[f.return_type]

        f.typeclass = FunctionType(f.name, return_type, args)

        for s in f.statements:
            self.visit_statement(s)

        self.symbols.pop_scope()

    def visit_statement(self, s: Node):
        if isinstance(s, Let):
            self.visit_let(s)
        else:
            self.visit_expr(s)

    def visit_let(self, s: Let):
        self.visit_expr(s.value)
        s.typeclass = s.value.typeclass
        self.symbols.define(s.name, s)

    def visit_expr(self, s):
        if isinstance(s, FunctionCall):
            f = self.symbols.lookup(s.name.value)
            assert (isinstance(f.typeclass, FunctionType))
            s.typeclass = f.typeclass.return_type
            [self.visit_expr(a) for a in s.args]
        if isinstance(s, Operator):
            self.visit_expr(s.left)
            self.visit_expr(s.right)
            assert (s.left.typeclass == s.right.typeclass)
            s.typeclass = s.left.typeclass
        if isinstance(s, Comparison):
            self.visit_expr(s.left)
            self.visit_expr(s.right)
            assert (s.left.typeclass == s.right.typeclass)
            s.typeclass = boolean
        if isinstance(s, IfElse):
            self.visit_expr(s.test)
            assert (s.test.typeclass == boolean)
            s.typeclass = void
            if len(s.if_statements) > 0:
                for t in s.if_statements:
                    self.visit_statement(t)
                s.typeclass = s.if_statements[-1].typeclass
            if len(s.else_statements) > 0:
                for t in s.else_statements:
                    self.visit_statement(t)
                assert(s.if_statements[-1].typeclass == s.else_statements[-1].typeclass)
        if isinstance(s, MemberAccess):
            self.visit_expr(s.source)
            field_index = s.source.typeclass.member_names[s.field];
            assert (isinstance(s.source.typeclass, StructType))
            s.typeclass = s.source.typeclass.members[field_index].typeclass
        if isinstance(s, Ident):
            t = self.symbols.lookup(s.value)
            s.typeclass = t.typeclass
        if isinstance(s, BooleanLiteral):
            s.typeclass = boolean
        if isinstance(s, NumericLiteral):
            s.typeclass = i32
        if isinstance(s, StringLiteral):
            s.typeclass = ArrayType(i8)
        if isinstance(s, StructLiteral):
            t = self.symbols.lookup(s.name)
            assert (isinstance(t.typeclass, StructType))
            s.typeclass = t.typeclass
