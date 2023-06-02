grammar Aevum;

module: declaration* EOF;

declaration: struct | function;

struct: 'struct' identifier '{' field_list '}';

field_list: field (',' field)* ','? |;

field: identifier ':' type;

type: identifier # BasicType | '[' type ']' # ArrayType;

function:
	'fn' identifier '(' arg_list ')' return_type '{' statement_list '}';

arg_list: arg (',' arg)* ','? |;

arg: identifier ':' type;

return_type: ('->' type)?;

statement_list: statement (';' statement)* ';'? |;

statement:
	'let' identifier '=' expr	# LetStatement
	| expr						# ExprStatement;

expr_list: expr (',' expr)* ','? |;

expr:
	expr '[' expr ']'			# ArrayIndex
	| expr '(' expr_list ')'	# FunctionCall
	| expr '.' identifier		# MemberAccess
	| expr ('*' | '/') expr		# Multplication
	| expr ('+' | '-') expr		# Addition
	| atom						# AtomExpr;

atom:
	identifier
	| number
	| string_literal
	| struct_literal
	| array_literal;

identifier: IDENT;

number: NUMBER;

string_literal: STRING;

struct_literal: identifier '{' field_initialiser_list '}';

field_initialiser_list:
	field_initialiser (',' field_initialiser)* ','?
	|;

field_initialiser: identifier ':' expr;

array_literal: '[' expr_list ']';

IDENT: [\p{ID_Start}][\p{ID_Continue}]*;
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["] | '\\"')* '"';
WS: [ \r\n]+ -> skip;
COMMENT: '//' (~'\n')* -> skip;
