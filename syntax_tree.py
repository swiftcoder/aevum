from dataclasses import dataclass
from typing import Any, TypeAlias, Union


@dataclass
class Variable:
    name: str


@dataclass
class Number:
    value: str


@dataclass
class StringLiteral:
    value: str


@dataclass
class Assignment:
    variable: str
    value: "Expr"


@dataclass
class StructLiteral:
    name: str
    fields: list[Assignment]


@dataclass
class ArrayLiteral:
    values: list["Expr"]


Literal: TypeAlias = Number | StringLiteral | StructLiteral | ArrayLiteral


@dataclass
class Operator:
    op: str
    left: "Expr"
    right: "Expr"


Expr: TypeAlias = Union[Literal, Variable, Operator, "MemberAccess", "FunctionCall"]


@dataclass
class MemberAccess:
    source: Expr
    fieldname: str


@dataclass
class ArrayIndex:
    source: Expr
    index: Expr


@dataclass
class FunctionCall:
    source: Expr
    arguments: list[Expr]


@dataclass
class Field:
    name: str
    typename: str


@dataclass
class Struct:
    name: str
    fields: list[Field]


@dataclass
class Function:
    name: str
    arguments: list[Field]
    return_type: str | None
    statements: list


@dataclass
class Module:
    declarations: list[Struct | Function]
