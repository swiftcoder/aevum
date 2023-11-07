
from dataclasses import dataclass
from typing import Optional
from llvmlite import ir


@dataclass(kw_only=True)
class BasicType(object):
    name: str
    llvm_type: ir.Type


void = BasicType(name='void', llvm_type=ir.VoidType())
boolean = BasicType(name='boolean', llvm_type=ir.IntType(1))
i8 = BasicType(name='i8', llvm_type=ir.IntType(8))
i32 = BasicType(name='i32', llvm_type=ir.IntType(32))

char_type = i8
ptr_size_type = i32

@dataclass
class ArrayType(BasicType):
    member_type: BasicType

    def __init__(self, member_type: BasicType):
        self.name = f"[{member_type.name}]"
        self.llvm_type = ir.LiteralStructType(
            [ptr_size_type.llvm_type, ir.PointerType(member_type.llvm_type)])
        self.member_type = member_type


@dataclass
class StructType(BasicType):
    members: list[BasicType]
    member_names: dict[str | int]

@dataclass
class FunctionType(BasicType):
    return_type: BasicType
    argument_types: list[BasicType]

    def __init__(self, name: str, return_type: BasicType, argument_types: list[BasicType]):
        self.name = f"function {name} ({argument_types}) -> {return_type}"
        self.llvm_type = ir.FunctionType(return_type.llvm_type, [a.llvm_type for a in argument_types])
        self.return_type = return_type
        self.argument_types = argument_types
