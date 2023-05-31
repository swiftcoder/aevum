
from enum import StrEnum
from dataclasses import dataclass
from collections import namedtuple
from more_itertools import peekable

class TokenType(StrEnum):
    Ident = "id"
    Number = "num"
    String = "str"
    Punctuation = "punct"
    Error = "error"

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int

ErrorToken = Token(TokenType.Error, "", 0, 0)

class LexerError(Exception):
    pass

def tokenize(code):
    line = 1
    column = 1

    input = peekable(code)
    while input:
        c = next(input)
        if c == '\n':
            line += 1
            column = 1
        elif c.isspace():
            column += 1
        elif c == '-' and input.peek() == '>':
            next(input)
            yield Token(TokenType.Punctuation, '->', line, column)
            column += 2
        elif c == '/' and input.peek() == '/':
            while input.peek() != '\n':
                next(input)
                column += 1
        elif c in ['{', '}', '(', ')', '[', ']', ':', ';', ',', '.', '=', '+', '-', '*', '/']:
            yield Token(TokenType.Punctuation, c, line, column)
            column += 1
        elif c.isdigit():
            num = c
            while input.peek().isdigit():
                num += next(input)
            if input.peek() == '.':
                num += next(input)
                while input.peek().isdigit():
                    num += next(input)
            yield Token(TokenType.Number, num, line, column)
            column += len(num)
        elif c.isalpha():
            ident = c
            while input.peek().isalnum():
                ident += next(input)
            yield Token(TokenType.Ident, ident, line, column)
            column += len(ident)
        elif c == '"':
            s = ""
            while not (input.peek() == '"' and c != '\\'):
                c = next(input)
                s += c
            next(input)
            yield Token(TokenType.String, s, line, column)
            column += len(s)+2
        else:
            raise LexerError(f'{c} unexpected on line {line} column {column}')
