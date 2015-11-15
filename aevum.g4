
grammar aevum;

top_level : (struct_def | cdecl | function_def)* EOF;

struct_def : STRUCT Identifier LBRACE struct_body RBRACE;

struct_body : var_decl (COMMA struct_body)?;
var_decl : Identifier COLON type_expr;

type_expr : Identifier;

cdecl : CDECL function_decl SEMICOLON;

function_def : function_decl block;
function_decl : FN Identifier function_args;
function_args : LPAREN function_arg_list? RPAREN;
function_arg_list : var_decl (COMMA function_arg_list)?;

block : LBRACE statement* RBRACE;

statement : (let_var | assignment | expression) SEMICOLON;

let_var : LET var_decl;

assignment : expression EQ expression;

expression_list : expression (COMMA expression_list)?;

expression : call_expression | dummy_member_expression;
call_expression : dummy_member_expression (LPAREN expression_list? RPAREN);
dummy_member_expression: member_expression | atom;
member_expression : atom DOT Identifier;
atom: named_reference | literal;
named_reference : Identifier;

STRUCT : 'struct';
FN : 'fn';
CDECL : 'cdecl';
LET : 'let';
LPAREN : '(';
RPAREN : ')';
COMMA : ',';
LBRACE : '{';
RBRACE : '}';
SEMICOLON : ';';
COLON : ':';
DOT : '.';
EQ : '=';

Identifier : (Identifier_start Identifier_char*);

fragment Identifier_start : [_a-zA-Z]
 | '\u00A8' | '\u00AA' | '\u00AD' | '\u00AF' | [\u00B2-\u00B5] | [\u00B7-\u00BA]
 | [\u00BC-\u00BE] | [\u00C0-\u00D6] | [\u00D8-\u00F6] | [\u00F8-\u00FF]
 | [\u0100-\u02FF] | [\u0370-\u167F] | [\u1681-\u180D] | [\u180F-\u1DBF]
 | [\u1E00-\u1FFF]
 | [\u200B-\u200D] | [\u202A-\u202E] | [\u203F-\u2040] | '\u2054' | [\u2060-\u206F]
 | [\u2070-\u20CF] | [\u2100-\u218F] | [\u2460-\u24FF] | [\u2776-\u2793]
 | [\u2C00-\u2DFF] | [\u2E80-\u2FFF]
 | [\u3004-\u3007] | [\u3021-\u302F] | [\u3031-\u303F] | [\u3040-\uD7FF]
 | [\uF900-\uFD3D] | [\uFD40-\uFDCF] | [\uFDF0-\uFE1F] | [\uFE30-\uFE44]
 | [\uFE47-\uFFFD];

fragment Identifier_char : [0-9]
 | [\u0300-\u036F] | [\u1DC0-\u1DFF] | [\u20D0-\u20FF] | [\uFE20-\uFE2F]
 | Identifier_start;

literal : (integer_literal | floating_point_literal | string_literal);
floating_point_literal : Floating_point_literal;
string_literal : String_literal;

integer_literal : Binary_literal | Octal_literal | Hexadecimal_literal | Decimal_literal;

Binary_literal : '0b' Binary_digit Binary_literal_chars*;
fragment Binary_digit : [01];
fragment Binary_literal_chars : Binary_digit | '_';

Octal_literal : '0o' Octal_digit Octal_literal_chars*;
fragment Octal_digit : [0-7];
fragment Octal_literal_chars : Octal_digit | '_';

Hexadecimal_literal : '0x' Hex_digit Hex_literal_chars*;
fragment Hex_digit : [0-9a-zA-Z];
fragment Hex_literal_chars : Hex_digit | '_';

Decimal_literal : Decimal_digit Decimal_literal_chars*;
fragment Decimal_digit : [0-9];
fragment Decimal_literal_chars : Decimal_digit | '_';

Floating_point_literal : Decimal_literal Decimal_fraction? Decimal_exponent?;
fragment Decimal_fraction : '.' Decimal_literal ;
fragment Decimal_exponent : [eE] [+\-]? Decimal_literal ;

String_literal : '"' (Escaped_quote | ~('\n'|'\r'))* '"';
fragment Escaped_quote : '\\"';

WS : [ \n\r\t] -> channel(HIDDEN);

Line_comment : '//' .*? '\n' -> channel(HIDDEN);

