import unittest

from syntax_tree import *
from lexer import tokenize
from parsing import parse


class TestParsing(unittest.TestCase):
    def test_empty(self):
        result, _ = parse(tokenize(r""))
        self.assertEqual(result, Module([]))

    def test_struct(self):
        result, _ = parse(
            tokenize(
                r"""
    struct Foo {
        foo: u32,
        bar: str
    }
    """
            )
        )
        self.assertEqual(
            result,
            Module([Struct("Foo", [Field("foo", "u32"), Field("bar", "str")])]),
        )

    def test_minimal_function(self):
        result, _ = parse(tokenize(r"fn func() {}"))
        self.assertEqual(
            result,
            Module([Function("func", [], None, [])]),
        )

    def test_maximal_function(self):
        result, _ = parse(tokenize(r"fn func(a: u32, b: str) -> str {a + b + c}"))
        self.assertEqual(
            result,
            Module(
                [
                    Function(
                        "func",
                        [Field("a", "u32"), Field("b", "str")],
                        "str",
                        [
                            Operator(
                                "+",
                                Variable("a"),
                                Operator("+", Variable("b"), Variable("c")),
                            )
                        ],
                    )
                ]
            ),
        )

    def test_array_access(self):
        result, _ = parse(tokenize(r"fn func() {arr[i]}"))
        self.assertEqual(
            result,
            Module(
                [
                    Function(
                        "func",
                        [],
                        None,
                        [ArrayIndex(Variable("arr"), Variable("i"))],
                    )
                ]
            ),
        )

    def test_function_call(self):
        result, _ = parse(tokenize(r"fn func() {func(i)}"))
        self.assertEqual(
            result,
            Module(
                [
                    Function(
                        "func",
                        [],
                        None,
                        [FunctionCall(Variable("func"), [Variable("i")])],
                    )
                ]
            ),
        )

    def test_chained_array_access(self):
        result, _ = parse(tokenize(r"fn func() {func(a)[i]}"))
        self.assertEqual(
            result,
            Module(
                [
                    Function(
                        "func",
                        [],
                        None,
                        [
                            ArrayIndex(
                                FunctionCall(Variable("func"), [Variable("a")]),
                                Variable("i"),
                            )
                        ],
                    )
                ]
            ),
        )

    def test_chained_operator(self):
        result, err = parse(tokenize(r"fn func() {arr[i] + 2}"))
        print(result)
        print(err)
        self.assertEqual(
            result,
            Module(
                [
                    Function(
                        "func",
                        [],
                        None,
                        [
                            Operator(
                                "+",
                                ArrayIndex(
                                    Variable("arr"),
                                    Variable("i"),
                                ),
                                Number("2"),
                            )
                        ],
                    )
                ]
            ),
        )


if __name__ == "__main__":
    unittest.main()
