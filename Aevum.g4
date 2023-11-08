grammar Aevum;

module: declaration* EOF;

declaration: struct | function;

struct: 'struct' identifier '{' variable_list '}';

variable_list: variable (',' variable)* ','? |;

variable: identifier ':' type;

type: identifier # BasicType | '[' type ']' # ArrayType;

function:
	'fn' identifier '(' variable_list ')' return_type '{' statement_list '}';

return_type: ('->' type)?;

statement_list: statement (';' statement)* ';'? |;

statement:
	'let' variable '=' expr		# LetStatement
	| expr						# ExprStatement;

expr_list: expr (',' expr)* ','? |;

expr:
	expr '[' expr ']'						# ArrayIndex
	| expr '(' expr_list ')'				# FunctionCall
	| expr '.' identifier					# MemberAccess
	| expr ('*' | '/') expr					# Multplication
	| expr ('+' | '-') expr					# Addition
	| expr ('==' | '!=' | '<' | '<=' | '>' | '>=') expr 	# Comparison
	| 'if' expr '{' statement_list '}' ('else' '{' statement_list '}')?		# IfElse
	| expr '=' expr 						# AssignExpr
	| '(' expr ')' 							# ParenthicalExpr
	| atom									# AtomExpr;

atom:
	identifier
	| boolean_literal
	| numeric_literal
	| string_literal
	| struct_literal
	| array_literal;

identifier: IDENT;

boolean_literal: 'true' | 'false';

numeric_literal: NUMBER;

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
