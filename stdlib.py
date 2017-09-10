
from llvmlite import ir
import type
import names

class TypeWrapper(object):
    def __init__(self, type):
        self.type = type

class Function(object):
    def __init__(self, name, args, result, module):
        self._name = name
        self.args = args

        mangled = names.mangle(name, [a.type.name for a in args])

        self.func_type = ir.FunctionType(result.type.irtype, (a.type.irtype for a in args), False)
        self.func = ir.Function(module, self.func_type, mangled)

    def typecheck(self, symboltable):
        pass

    def typecheck_body(self, symboltable):
        pass

    def call(self, builder, stack):
        count = len(self.func.args)
        if count > 0:
            args = stack[-count:]
            del stack[-count:]
        else:
            args = []
        stack.append(builder.call(self.func, args))

    def __repr__(self):
        return 'stdfunc %s' % (self._name)

def int_cmp(name, op, symboltable, dependencies, module):
    bool_type = TypeWrapper(type.BoolType)
    num_type = TypeWrapper(type.Int32Type)

    f = Function(name, (num_type, num_type), bool_type, module)

    block = f.func.append_basic_block('entry')
    builder = ir.IRBuilder(block)
    e = builder.icmp_signed(op, f.func.args[0], f.func.args[1])
    builder.ret(e)

    symboltable.put(name, f)
    dependencies.append((f, []))

def standard_library(symboltable, dependencies, module):
    int_cmp('__eq__', '==', symboltable, dependencies, module)
    int_cmp('__neq__', '!=', symboltable, dependencies, module)
