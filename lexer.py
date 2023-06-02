from enum import StrEnum, auto
from dataclasses import dataclass
from collections import namedtuple
from more_itertools import peekable


class TokenType(StrEnum):
    Ident = auto()
    Keyword = auto()
    Number = auto()
    String = auto()
    Punctuation = auto()
    Error = auto()

    def __repr__(self) -> str:
        return self.__str__().title()


@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int

    def __repr__(self) -> str:
        return f"{self.type}({self.value})"


ErrorToken = Token(TokenType.Error, "", 0, 0)

Keywords = ["struct", "fn", "let"]


class LexerError(Exception):
    pass


def tokenize(code):
    line = 1
    column = 1

    input = peekable(code)
    while input:
        c = next(input)
        if c == "\n":
            line += 1
            column = 1
        elif c.isspace():
            column += 1
        elif c == "-" and input.peek() == ">":
            next(input)
            yield Token(TokenType.Punctuation, "->", line, column)
            column += 2
        elif c == "/" and input.peek() == "/":
            while input.peek() != "\n":
                next(input)
                column += 1
        elif c in [
            "{",
            "}",
            "(",
            ")",
            "[",
            "]",
            ":",
            ";",
            ",",
            ".",
            "=",
            "+",
            "-",
            "*",
            "/",
        ]:
            yield Token(TokenType.Punctuation, c, line, column)
            column += 1
        elif c.isdigit():
            num = c
            while input.peek().isdigit():
                num += next(input)
            if input.peek() == ".":
                num += next(input)
                while input.peek().isdigit():
                    num += next(input)
            yield Token(TokenType.Number, num, line, column)
            column += len(num)
        elif c.isalpha():
            ident = c
            while input.peek().isalnum():
                ident += next(input)
            if ident in Keywords:
                yield Token(TokenType.Keyword, ident, line, column)
            else:
                yield Token(TokenType.Ident, ident, line, column)
            column += len(ident)
        elif c == '"':
            s = ""
            while not (input.peek() == '"' and c != "\\"):
                c = next(input)
                s += c
            next(input)
            yield Token(TokenType.String, s, line, column)
            column += len(s) + 2
        else:
            raise LexerError(f"{c} unexpected on line {line} column {column}")
