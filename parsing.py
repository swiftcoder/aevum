from lexer import TokenType, ErrorToken, Token

from more_itertools import seekable
from dataclasses import dataclass
from typing import Any, Callable

from syntax_tree import *
from combinators import *


def print_node(prompt):
    def print_node_(x):
        print(f"{prompt} {x}")
        return x

    return print_node_


def parse(input: list[Token]):
    tokens = ParseInput(input)

    stack = list()

    def push(p):
        stack.append(p)
        return p

    def pop(*p):
        return stack.pop()

    (set_expr_p, expr_p) = forward()

    field_initialiser_p = seq(ident(), punctuation(":"), expr_p)[
        lambda x: Assignment(x[0].value, x[2])
    ]

    struct_literal_p = seq(
        ident(),
        punctuation("{"),
        separated_by(seq(field_initialiser_p), punctuation(",")),
        punctuation("}"),
    )[lambda x: StructLiteral(x[0].value, x[2])]

    array_literal_p = seq(
        punctuation("["), separated_by(expr_p, punctuation(",")), punctuation("]")
    )[lambda a: ArrayLiteral(a[1])]

    atom_p = choice(
        struct_literal_p,
        array_literal_p,
        ident()[lambda x: Variable(x.value)],
        number()[lambda n: Number(n.value)],
        string()[lambda s: StringLiteral(s.value)],
        seq(punctuation("("), expr_p, punctuation(")"))[lambda x: x[1]],
        # expr_p,
    ).tag("atom")

    factor_p = choice(
        seq(atom_p, choice(punctuation("+"), punctuation("-")), expr_p)[
            lambda v: Operator(v[1].value, v[0], v[2])
        ],
        atom_p,
    ).tag("factor")

    partial_expr_p = choice(
        seq(factor_p, choice(punctuation("*"), punctuation("/")), expr_p)[
            lambda v: Operator(v[1].value, v[0], v[2])
        ],
        factor_p,
    ).tag("partisl_expr")

    # set_expr_prime_p, expr_prime_p = forward()
    # set_expr_prime_p(
    #     optional(
    #         choice(
    #             seq(
    #                 seq(punctuation("."), ident())[
    #                     lambda x: MemberAccess(pop(), x[1].value)
    #                 ][push],
    #                 expr_prime_p,
    #             ),
    #             seq(
    #                 seq(
    #                     punctuation("("),
    #                     separated_by(expr_p, punctuation(",")),
    #                     punctuation(")"),
    #                 )[lambda x: FunctionCall(pop(), x[1])][push],
    #                 expr_prime_p,
    #             ),
    #             seq(
    #                 seq(punctuation("["), expr_p, punctuation("]"))[
    #                     lambda x: ArrayIndex(pop(), x[1])
    #                 ][push],
    #                 expr_prime_p,
    #             ),
    #         )
    #     )
    # )

    # set_expr_p(seq(partial_expr_p[push], expr_prime_p)[pop])

    set_expr_p(
        choice(
            seq(
                partial_expr_p[push],
                optional(
                    choice(
                        seq(punctuation("."), ident())[
                            lambda x: MemberAccess(pop(), x[1].value)
                        ][push],
                        seq(
                            punctuation("("),
                            separated_by(expr_p, punctuation(",")),
                            punctuation(")"),
                        )[lambda x: FunctionCall(pop(), x[1])][push],
                        seq(punctuation("["), expr_p, punctuation("]"))[
                            lambda x: ArrayIndex(pop(), x[1])
                        ][push],
                    )
                ),
            )[pop],
        )
    )

    # p = p . ident | p ( args ) | expr
    # p = expr !( (. ident) | ( (args)))

    assign_p = seq(keyword("let"), ident(), punctuation("="), expr_p)[
        lambda x: Assignment(x[1].value, x[3])
    ]

    statement_p = choice(assign_p, expr_p).tag("statement")

    field_p = seq(ident(), punctuation(":"), ident())[
        lambda v: Field(v[0].value, v[2].value)
    ]

    struct_p = seq(
        keyword("struct"),
        ident(),
        punctuation("{"),
        separated_by(field_p, punctuation(",")),
        punctuation("}"),
    )[lambda v: Struct(v[1].value, v[3])].tag("struct")

    func_p = (
        seq(
            keyword("fn"),
            ident(),
            punctuation("("),
            separated_by(field_p, punctuation(",")),
            punctuation(")"),
            optional(seq(punctuation("->"), ident())[lambda v: v[1].value]),
            punctuation("{"),
            separated_by(statement_p, punctuation(";").tag("semicolon")).tag(
                "statement_list"
            ),
            punctuation("}").tag("func closing brace"),
        )
        .tag("func_seq")[lambda v: Function(v[1].value, v[3], v[5], v[7])]
        .tag("func")
    )

    module_p = seq(zero_or_more(choice(struct_p, func_p)), eof())[
        lambda x: Module(x[0])
    ].tag("module")

    return module_p(tokens)


def punctuation(sample):
    def punctuation_parser(tokens):
        c = tokens.peek(ErrorToken)
        if c.type == TokenType.Punctuation and c.value == sample:
            return ParseResult(next(tokens), 1, [])
        return ParseResult(MATCH_FAILED, 0, [ParseError(f"{c} is not punctuation")])

    return Parser(punctuation_parser)


def keyword(sample):
    def keyword_parser(tokens):
        c = tokens.peek(ErrorToken)
        if c.type == TokenType.Ident and c.value == sample:
            return ParseResult(next(tokens), 1, [])
        return ParseResult(MATCH_FAILED, 0, [ParseError(f"{c} is not a keyword")])

    return Parser(keyword_parser)


def ident():
    def ident_parser(tokens):
        c = tokens.peek(ErrorToken)
        if c.type == TokenType.Ident:
            return ParseResult(next(tokens), 1, [])
        return ParseResult(MATCH_FAILED, 0, [ParseError(f"{c} is not an identifier")])

    return Parser(ident_parser)


def number():
    def number_parser(tokens):
        c = tokens.peek(ErrorToken)
        if c.type == TokenType.Number:
            return ParseResult(next(tokens), 1, [])
        return ParseResult(MATCH_FAILED, 0, [ParseError(f"{c} is not a number")])

    return Parser(number_parser)


def string():
    def string_parser(tokens):
        c = tokens.peek(ErrorToken)
        if c.type == TokenType.String:
            return ParseResult(next(tokens), 1, [])
        return ParseResult(MATCH_FAILED, 0, [ParseError(f"{c} is not a string")])

    return Parser(string_parser)
