
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

    def __repr__(self):
        return self.name

BoolType = BasicType('bool', ir.IntType(1))
Int32Type = BasicType('i32', ir.IntType(32))
FloatType = BasicType('f32', ir.FloatType())
StringType = BasicType('str', ir.IntType(8).as_pointer())

class StructType(BasicType):
    def __init__(self, name, members, irtype):
        super().__init__(name, irtype)
        self.members = members

def builtin_types():
    return [BoolType, Int32Type, FloatType, StringType]

def builtins():
    symbols = SymbolTable(None)
    for t in builtin_types():
        symbols.put(t.name, t);
    return symbols
