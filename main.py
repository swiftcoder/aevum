# code = r"""
# struct Foo {
#     data: u32,
#     log: str,
#     array: [u32]
# }

# struct Bar {
#     data: u32,
# }

# fn main() {
#     // this is a comment to be ignored!
#     let foo = Foo{data: 5};
#     let arr = [1, 2, 3, 4,];
#     let sum = add(2, 6);
#     let sum = add(foo.data, 7);
#     println(sum);
#     println("Hello, \"World\"!\n");
#     println(arr[sum + 1] + 2);
# }
# """

code = """
struct Foo {
    data: i32,
    log: str,
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    let foo = Foo{data: 5, log: "hello"};
    add(2, foo.data);
    println("Hello, world!");
    println("it's a wonderful world");
    let i = 5;
    if i < 10 {
        println("inside if statement");
    } else {
        println("inside else clause");
    }
}
"""

import sys
from pprint import pprint
from antlr4 import *
from AevumLexer import AevumLexer
from AevumParser import AevumParser
from abstract_syntax_tree import build_ast
import encode
from module import build_module
from symbols import setup_symbol_table
import typecheck


input = InputStream(code)
lexer = AevumLexer(input)
tokens = CommonTokenStream(lexer)
parser = AevumParser(tokens)
tree = parser.module()

ast = build_ast(tree)
ir = build_module("__main__", ast)
symbols = setup_symbol_table()
# pprint(ast)
for idx, line in enumerate(ir.split("\n")):
    print(idx + 1, line)

import llvmlite.binding as llvm
from ctypes import CFUNCTYPE, c_int32, c_void_p, string_at, cast

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()


def println(l: c_int32, s: c_void_p):
    value = string_at(s, l)
    print(value.decode())


println_type = CFUNCTYPE(None, c_int32, c_void_p)
println_func = println_type(println)

lljit = llvm.create_lljit_compiler()
rt = (
    llvm.JITLibraryBuilder()
    .add_ir(ir)
    .export_symbol("main")
    .import_symbol("println", cast(println_func, c_void_p).value)
    .link(lljit, "__main__")
)

main_type = CFUNCTYPE(None)
main_func = main_type(rt["main"])

main_func()
