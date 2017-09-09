
from llvmlite import ir
from symbols import SymbolTable

class BasicType(object):
    def __init__(self, name, irtype):
        self.name = name
        self.irtype = irtype

    def typecheck(self, symboltable):
        pass

    def emit_type(self):
        return self.irtype

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __repr__(self):
        return self.name

VoidType = BasicType('void', ir.VoidType())
BoolType = BasicType('bool', ir.IntType(1))
Int8Type = BasicType('i8', ir.IntType(8))
Int32Type = BasicType('i32', ir.IntType(32))
FloatType = BasicType('f32', ir.FloatType())
StringType = BasicType('str', ir.IntType(8).as_pointer())

class StructType(BasicType):
    def __init__(self, name, members, irtype):
        super().__init__(name, irtype)
        self.members = members

class ArrayType(BasicType):
    def __init__(self, innerType):
        name = 'array_of_' + str(innerType)
        irtype = ir.LiteralStructType([ir.IntType(32), innerType.irtype.as_pointer()])

        super().__init__(name, irtype)
        self.innerType = innerType

def builtin_types():
    return [VoidType, BoolType, Int8Type, Int32Type, FloatType, StringType]

def builtins():
    symbols = SymbolTable(None)
    for t in builtin_types():
        symbols.put(t.name, t);
    return symbols
