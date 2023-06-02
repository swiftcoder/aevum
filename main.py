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
fn add(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {
    println("Hello, world!");
    println("it's a wonderful world");
}
"""

import sys
from antlr4 import *
from AevumLexer import AevumLexer
from AevumParser import AevumParser
import encode


input = InputStream(code)
lexer = AevumLexer(input)
tokens = CommonTokenStream(lexer)
parser = AevumParser(tokens)
tree = parser.module()

wat = encode.encode(tree, parser)
print(wat)

from wasmer import (
    engine,
    Store,
    Module,
    Instance,
    ImportObject,
    Function,
    Memory,
    MemoryType,
)

store = Store()
module = Module(store, wat)
memory = Memory(store, MemoryType(minimum=1))


def println(start: int, length: int):
    s = bytearray(memory.uint8_view(offset=start)[:length]).decode()
    print(s)


imports = ImportObject()
imports.register("runtime", {"memory": memory})
imports.register("", {"println": Function(store, println)})

instance = Instance(module, imports)

instance.exports.main()
