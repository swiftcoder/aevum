#! /usr/bin/env python3

import ply.lex as lex
import re

reserved = {
    'struct': 'STRUCT',
    'fn': 'FN',
    'cdecl': 'CDECL',
    'let': 'LET',
    'true': 'TRUE',
    'false': 'FALSE',
    'if': 'IF',
    'else': 'ELSE',
}

tokens = [
    'IDENTIFIER', 'NUMERIC', 'STRING',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSQUARE', 'RSQUARE',
    'SEMICOLON', 'COLON', 'DOT', 'COMMA', 'ASSIGN', 'RARROW',
    'EQUALS', 'NEQUALS'
] + list(reserved.values())

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_COMMA = r','
t_ASSIGN = r'='
t_RARROW = r'->'
t_EQUALS = r'=='
t_NEQUALS = r'!='

def t_IDENTIFIER(t):
    r'[^\W0-9]\w*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

t_NUMERIC = r'(0[xb]?)?[0-9a-fA-F]+(\.[0-9a-fA-F]*(e[0-9a-fA-F]*)?)?'

t_STRING = r'"(\\.|[^\"])*"'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ignore_COMMENT(t):
    r'//[^\n]*'

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.UNICODE, debug=0)

if __name__ == '__main__':
     lex.runmain()
