
from llvmlite import ir
from abstract_syntax_tree import Argument, Function
from encode import Encoder
from symbols import SymbolTable

from typecheck import TypeChecker
from typenames import ArrayType, FunctionType, void, i8


def build_module(name: str, ast: list[Function]) -> str:
    module = ir.Module(name=name)

    symbols = SymbolTable()

    symbols.define(
        "println",
        Function(
            "println",
            [Argument("arg0", "str")],
            None,
            [],
            typeclass=FunctionType("println", void, [ArrayType(i8)]),
            llvm_value=ir.Function(
                module,
                ir.FunctionType(ir.VoidType(), [ArrayType(i8).llvm_type]),
                "println",
            ),
        ),
    )

    type_checker = TypeChecker(module, symbols)
    type_checker.visit_ast(ast)

    encoder = Encoder(module, symbols)
    encoder.visit_ast(ast)

    return str(encoder)
