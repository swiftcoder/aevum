
import pprint
from combinators import MATCH_FAILED
from lexer import tokenize
from parsing import parse
import sys

sys.setrecursionlimit(2000)

code = r"""
//struct Foo {
//    data: u32,
//}

//struct Bar {
//    data: u32,
//}

//fn add(a: u32, b: u32) -> u32 {
//    let c = 5;
//    a + b;
//}

fn main() {
    // this is a comment to be ignored!
    //let foo = Foo{data: 5};
    //let arr = [1, 2, 3, 4];
    //let sum = add(2, 6);
    //let sum = add(foo.data, 7);
    //println(sum);
    //println("Hello, \"World\"!\n");
    //println(arr[sum + 1] + 2)
    arr[1]
}
"""

# for i, t in enumerate(tokenize(code)):
#     print(i, t)

tokens = tokenize(code)

ast = parse(list(tokens))
if ast.result == MATCH_FAILED:
    print(ast.errors)
else:
    pprint.pprint(ast.result)
