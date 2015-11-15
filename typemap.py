
from llvmlite import ir
from symbols import SymbolTable

class BasicType(object):
    def __init__(self, name, _type):
        self.name = name
        self.type = _type

    def emit_type(self):
        return self.type

Int32Type = BasicType('i32', ir.IntType(32))
FloatType = BasicType('f32', ir.FloatType())
StrType = BasicType('str', ir.IntType(8).as_pointer())

def builtins():
    symbols = SymbolTable(None)
    symbols['i32'] = Int32Type
    symbols['f32'] = FloatType
    symbols['str'] = StrType
    return symbols
