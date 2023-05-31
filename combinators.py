from dataclasses import dataclass, field
import types
from typing import Any, Callable, Iterable

from more_itertools import seekable

MATCH_FAILED = object()


class ParseError(Exception):
    pass

@dataclass
class ParseInput:
    tokens: Any
    length: int

    def __init__(self, tokens: list[Any]):
        self.length = len(tokens)
        self.tokens = seekable(tokens)
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return next(self.tokens)
    
    def __bool__(self):
        return bool(self.tokens)
    
    def index(self) -> int:
        return self.tokens._index or 0
    
    def seek(self, index: int):
        self.tokens.seek(index)
    
    def peek(self, default):
        return self.tokens.peek(default)

@dataclass
class ParseResult:
    result: Any
    length: int
    errors: list[ParseError]


_memo: dict[Any, ParseResult] = dict()
_counters: dict[Any, int] = dict()


@dataclass(unsafe_hash=True)
class Parser:
    func: Callable
    name: str = ""

    def tag(self, name):
        self.name = name
        return self

    def __call__(self, tokens: ParseInput) -> ParseResult:
        index = tokens.index()

        if (self, index) in _memo:
            m = _memo[(self, index)]
            # print(
            #     f"returning memoised result {m} for ({self.name or id(self)}, {index})"
            # )
            tokens.seek(index + m.length)
            return m

        if _counters.setdefault((self, index), 0) > len(tokens) - index + 1:
            return ParseResult(
                MATCH_FAILED,
                0,
                [
                    ParseError(
                        f"recursion limit reached for {self.name or id(self)}@{index}"
                    )
                ],
            )

        _counters[(self, index)] = _counters[(self, index)] + 1
        print(f"{self.name or id(self)}@{index} -> {_counters[(self, index)]} < {len(tokens)}")

        result = self.func(tokens)
        # print(
        #     f"memoizing result {result.result} for ({self.name or id(self)}, {index})"
        # )
        _memo[(self, index)] = result
        return result

    def __getitem__(self, key: Callable) -> "Parser":
        return map(self, key)


def choice(*parsers):
    def choice_parser(tokens):
        errors = []
        for p in parsers:
            result = p(tokens)
            errors.extend(result.errors)
            if result.result != MATCH_FAILED:
                return result

        return ParseResult(
            MATCH_FAILED, 0, errors + [ParseError("none of the choices matched")]
        )

    return Parser(choice_parser)


def seq(*parsers: Parser):
    def seq_parser(tokens: ParseInput):
        index = tokens.index()
        result = []
        errors = []
        length = 0
        for p in parsers:
            c = p(tokens)
            errors.extend(c.errors)
            if c.result == MATCH_FAILED:
                # print(f"seeking back {tokens._index or 0 - index}")
                tokens.seek(index)
                return c
            result.append(c.result)
            length += c.length
        return ParseResult(result, length, [])

    return Parser(seq_parser)


def optional(parser: Parser):
    def optional_parser(tokens):
        result = parser(tokens)
        if result.result == MATCH_FAILED:
            return ParseResult(None, 0, result.errors)
        return result

    return Parser(optional_parser)


def zero_or_more(parser: Parser):
    def zero_or_more_parser(tokens):
        result = []
        errors = []
        length = 0
        while True:
            c = parser(tokens)
            if c.result == MATCH_FAILED:
                break
            result.append(c.result)
            errors.extend(c.errors)
            length += c.length
        return ParseResult(result, length, errors)

    return Parser(zero_or_more_parser)


def separated_by(parser: Parser, separator: Parser):
    def separated_by_parser(tokens):
        result = []
        errors = []
        length = 0
        while True:
            c = parser(tokens)
            errors.extend(c.errors)
            if c.result != MATCH_FAILED:
                result.append(c.result)
                length += c.length

                s = separator(tokens)
                errors.extend(s.errors)
                if s.result == MATCH_FAILED:
                    break
                else:
                    length += s.length
            else:
                break
        return ParseResult(result, length, errors)

    return Parser(separated_by_parser)


# def skip_until(parser):
#     def skip_until_parser(tokens):
#         errors = []
#         while tokens:
#             c, errs = parser(tokens)
#             errors.extend(errs)
#             if c != MATCH_FAILED:
#                 return c, errors
#             next(tokens)
#     return Parser(skip_until_parser)


def eof():
    def eof_parser(tokens):
        if not tokens:
            return ParseResult(None, 0, [])
        return ParseResult(
            MATCH_FAILED, 0, [ParseError("input is not at end of stream")]
        )

    return Parser(eof_parser)


def map(parser: Parser, f: Callable):
    def map_parser(tokens):
        result = parser(tokens)
        if result.result != MATCH_FAILED:
            return ParseResult(f(result.result), result.length, result.errors)
        return result

    return Parser(map_parser)


def forward() -> tuple[Callable, Parser]:
    p: list[Parser | None] = [None]

    def set_parser(parser: Parser):
        p[0] = parser

    def forward_parser(tokens):
        return p[0](tokens)

    return (set_parser, Parser(forward_parser))
