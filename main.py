
code = """
struct Foo {
    data: i32,
    log: str,
    number: i32
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn loop() {
    let i : i32 = 0;
    while i < 3 {
        println("loop iteration");
        i = i + 1;
    };
    println("loop done");
}

fn main() {
    let foo : Foo = Foo{data: 5, log: "hello", number: 11};
    add(2, foo.data);
    println("Hello, world!");
    println("it's a wonderful world");
    if (foo.number - 2) < 10 {
        println("inside if statement");
        add(2, 3);
    } else {
        println("inside else clause");
        2;
    };

    loop();
}
"""

import sys
from pprint import pprint
from antlr4 import InputStream, CommonTokenStream
from AevumLexer import AevumLexer
from AevumParser import AevumParser
from abstract_syntax_tree import build_ast
import encode
from module import build_module
import typecheck


input = InputStream(code)
lexer = AevumLexer(input)
tokens = CommonTokenStream(lexer)
parser = AevumParser(tokens)
tree = parser.module()

ast = build_ast(tree)
ir = build_module("__main__", ast)
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
