#! /usr/bin/env python3

import ply.yacc as yacc

from lexer import tokens
from ast import *

def p_top_level_list_empty(p):
    'top_level_list : '
    p[0] = []
def p_top_level_list_one(p):
    'top_level_list : top_level_item'
    p[0] = [p[1]]
def p_top_level_list_rest(p):
    'top_level_list : top_level_list top_level_item'
    p[0] = p[1]
    p[0].append(p[2])

def p_top_level_item(p):
    '''top_level_item : struct_def
                      | cdecl
                      | function_def'''
    p[0] = p[1]

def p_struct_def(p):
    'struct_def : STRUCT identifier LBRACE struct_body RBRACE'
    p[0] = Struct(p[2], p[4])

def p_struct_body_empty(p):
    'struct_body : '
    p[0] = []
def p_struct_body_one(p):
    'struct_body : var_decl'
    p[0] = [p[1]]
def p_struct_body_rest(p):
    'struct_body : struct_body COMMA var_decl'
    p[0] = p[1]
    p[1].append(p[3])

def p_var_decl(p):
    'var_decl : identifier COLON type_expr'
    p[0] = VarDecl(p[1], p[3])

def p_typeexpr(p):
    'type_expr : identifier'
    p[0] = p[1]

def p_cdecl(p):
    'cdecl : CDECL function_decl SEMICOLON'
    p[0] = CFunction(*p[2])

def p_function_def(p):
    'function_def : function_decl block'
    p[0] = Function(p[1][0], p[1][1], p[2])

def p_function_decl(p):
    'function_decl : FN identifier function_args'
    p[0] = (p[2], p[3])

def p_function_args(p):
    'function_args : LPAREN function_arg_list RPAREN'
    p[0] = p[2]

def p_function_arg_list_empty(p):
    'function_arg_list :'
    p[0] = []
def p_function_arg_list_one(p):
    'function_arg_list : var_decl'
    p[0] = [p[1]]
def p_function_arg_list_rest(p):
    'function_arg_list : function_arg_list COMMA var_decl'
    p[0] = p[1]
    p[0].append(p[3])

def p_block(p):
    'block : LBRACE statement_list RBRACE'
    p[0] = p[2]

def p_statement_list_empty(p):
    'statement_list : '
    p[0] = []
def p_statement_list_one(p):
    'statement_list : statement SEMICOLON'
    p[0] = [p[1]]
def p_statement_list_rest(p):
    'statement_list : statement_list statement SEMICOLON'
    p[0] = p[1]
    p[0].append(p[2])

def p_statement(p):
    '''statement : let_var
                 | assignment
                 | expression'''
    p[0] = p[1]

def p_let_var(p):
    'let_var : LET var_decl'
    p[0] = p[2]

def p_assignment(p):
    'assignment : expression ASSIGN expression'
    p[0] = Assignment(p[1], p[3])

def p_expression_list_one(p):
    'expression_list : expression'
    p[0] = [p[1]]
def p_expression_list_rest(p):
    'expression_list : expression_list COMMA expression'
    p[0] = p[1]
    p[0].append(p[2])

def p_expression(p):
    '''expression : call_expression
                  | dummy_member_expression'''
    p[0] = p[1]

def p_call_expression_no_args(p):
    'call_expression : dummy_member_expression LPAREN RPAREN'
    p[0] = Call(p[1], None)
def p_call_expression(p):
    'call_expression : dummy_member_expression LPAREN expression_list RPAREN'
    p[0] = Call(p[1], p[3])

def p_dummy_member_expression(p):
    '''dummy_member_expression : member_expression
                               | atom'''
    p[0] = p[1]

def p_member_expression(p):
    'member_expression : atom DOT identifier'
    p[0] = Member(p[1], p[3])

def p_atom(p):
    '''atom : named_reference
            | literal'''
    p[0] = p[1]

def p_named_reference(p):
    'named_reference : identifier'
    p[0] = VarRef(p[1])

def p_identifier(p):
    'identifier : IDENTIFIER'
    p[0] = p[1]

def p_literal(p):
    '''literal : numeric
               | string
               | bool'''
    p[0] = p[1]

def p_numeric(p):
    'numeric : NUMERIC'
    if any(c in p[1] for c in ['.', 'e']):
        p[0] = ConstantFloat(p[1])
    else:
        p[0] = ConstantInt(p[1])

def p_string(p):
    'string : STRING'
    p[0] = ConstantString(p[1])

def p_bool_true(p):
    'bool : TRUE'
    p[0] = ConstantBool(True)
def p_bool_false(p):
    'bool : FALSE'
    p[0] = ConstantBool(False)

def p_error(p):
    print("Syntax error in input!")

yacc.yacc(debug=1)

if __name__ == '__main__':
    import logging
    import sys
    from pathlib import Path

    log = logging.getLogger()
    ast = yacc.parse(Path(sys.argv[1]).read_text(), debug=log)

    print('\n' + '\n\n'.join(str(s) for s in ast))
