
from llvmlite import ir
from symbols import SymbolTable

class BasicType(object):
    def __init__(self, name, irtype):
        self.name = name
        self.irtype = irtype

    def emit_type(self):
        return self.irtype

Int32Type = BasicType('i32', ir.IntType(32))
FloatType = BasicType('f32', ir.FloatType())
StrType = BasicType('str', ir.IntType(8).as_pointer())

class StructType(BasicType):
    def __init__(self, name, members, irtype):
        super().__init__(name, irtype)
        self.members = members

def builtins():
    symbols = SymbolTable(None)
    symbols['i32'] = Int32Type
    symbols['f32'] = FloatType
    symbols['str'] = StrType
    return symbols
