
import sys

from llvmlite import ir

from symbols import *
from typemap import *

next_serial = 1

class ConstantString(object):
    def __init__(self, data):
        data = data[1:-1]
        self.data = data.replace('\\\"', '\"') + '\0'

    def typecheck(self, symboltable):
        pass

    def emit(self, builder, stack):
        global next_serial
        name = 'string_constant_%d' % (next_serial)
        next_serial += 1

        t = ir.ArrayType(ir.IntType(8), len(self.data))
        glob = ir.GlobalVariable(builder.module, t, name=name)
        glob.global_constant = True
        glob.initializer = ir.Constant(t, bytearray(self.data, 'utf-8'))
        z = ir.Constant(ir.IntType(32), 0)
        g = builder.gep(glob, [z, z])
        stack.append(g)

    def __repr__(self):
        return 'string "%s"' % (self.data)

class ConstantInt(object):
    def __init__(self, value):
        self.value = int(value)

    def typecheck(self, symboltable):
        pass

    def emit(self, builder, stack):
        i = ir.Constant(ir.IntType(32), self.value)
        stack.append(i)

    def __repr__(self):
        return 'int %s' % (self.value)

class ConstantFloat(object):
    def __init__(self, value):
        if value.startswith('0x') or value.startswith('0X'):
            self.value = float.fromhex(value)
        else:
            self.value = float(value)

    def typecheck(self, symboltable):
        pass

    def emit(self, builder, stack):
        i = ir.Constant(ir.FloatType(), self.value)
        stack.append(i)

    def __repr__(self):
        return 'float %s' % (self.value)

class VarRef(object):
    def __init__(self, name):
        self.name = name

    def typecheck(self, symboltable):
        self.item = symboltable[self.name]

    def emit(self, builder, stack):
        pass

    def fetch(self, builder, stack):
        self.item.fetch(builder, stack)

    def call(self, builder, stack):
        self.item.call(builder, stack)

    def reference(self, builder):
        return self.item.reference(builder)

    def __repr__(self):
        return 'var %s' % (self.name)

class Member(object):
    def __init__(self, target, name):
        self.target = target
        self.name = name

    def typecheck(self, symboltable):
        self.target.typecheck(symboltable)
        self.item = self.target.item.type.members[self.name]
        self.index = list(self.target.item.type.members.keys()).index(self.name)

    def emit(self, builder, stack):
        g = self.reference(builder)
        stack.append(builder.load(g))

    def reference(self, builder):
        z = ir.Constant(ir.IntType(32), 0)
        i = ir.Constant(ir.IntType(32), self.index)
        g = builder.gep(self.target.item.item, [z, i])
        return g

    def __repr__(self):
        return '%s.%s' % (str(self.target), self.name)

class Call(object):
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def typecheck(self, symboltable):
        self.func.typecheck(symboltable)
        for a in self.args:
            a.typecheck(symboltable)

    def emit(self, builder, stack):
        for a in self.args:
            a.emit(builder, stack)
        self.func.call(builder, stack)

    def __repr__(self):
        args = ', '.join(str(a) for a in self.args) if self.args else ''
        return '%s(%s)' % (str(self.func), args)

class VarDecl(object):
    def __init__(self, name, _type):
        self.name = name
        self.type = _type

    def typecheck(self, symboltable):
        self.type = symboltable[self.type]
        symboltable[self.name] = self

    def emit(self, builder, stack):
        self.item = builder.alloca(self.type.irtype)
        stack.append(builder.load(self.item))

    def fetch(self, builder, stack):
        stack.append(builder.load(self.item))

    def reference(self, builder):
        return self.item

    def __repr__(self):
        return '%s : %s' % (self.name, self.type)

class Assignment(object):
    def __init__(self, target, value):
        self.target = target
        self.value = value

    def typecheck(self, symboltable):
        self.target.typecheck(symboltable)
        self.value.typecheck(symboltable)

    def emit(self, builder, stack):
        t = self.target.reference(builder)
        self.value.emit(builder, stack)
        v = stack.pop()
        builder.store(v, t)

    def __repr__(self):
        return '%s = %s' % (self.target, self.value)

class Struct(object):
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def typecheck(self, typemap):
        for m in self.members:
            m.typecheck(typemap)

        self.irtype = ir.LiteralStructType(m.type.irtype for m in self.members)
        self.type = StructType(self.name, {m.name: m.type for m in self.members}, self.irtype)
        typemap[self.name] = self.type

    def emit(self, module):
        pass

    def __repr__(self):
        members = ', '.join(str(s) for s in self.members) if self.members else ''
        return 'struct %s {%s}' % (self.name, members)

class Function(object):
    def __init__(self, name, args, body, symboltable):
        self.name = name
        self.args = args
        self.body = body
        self.symboltable = SymbolTable(symboltable)

    def typecheck(self, typemap):
        for a in self.args:
            a.typecheck(typemap)
            self.symboltable[a.name] = a

        for b in self.body:
            b.typecheck(self.symboltable)

        self.irtype = ir.FunctionType(ir.VoidType(), (a.type.irtype for a in self.args), False)
        typemap[self.name] = self

    def emit(self, module):
        self.func = ir.Function(module, self.irtype, self.name)
        block = self.func.append_basic_block('entry')
        builder = ir.IRBuilder(block)
        for a, i in zip(self.args, self.func.args):
            t = builder.alloca(a.type.irtype)
            builder.store(i, t)
            a.item = t
        stack = []
        for b in self.body:
            b.emit(builder, stack)
        builder.ret_void()

    def call(self, builder, stack):
        count = len(self.func.args)
        args = stack[-count:]
        del stack[-count:]
        stack.append(builder.call(self.func, args))

    def __repr__(self):
        args = ', '.join(str(a) for a in self.args) if self.args else ''
        body = '; '.join(str(s) for s in self.body) + ';' if self.body else ''
        return 'fn %s(%s) {%s}' % (self.name, args, body)

class CFunction(object):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def typecheck(self, typemap):
        for a in self.args:
            a.typecheck(typemap)

        self.irtype = ir.FunctionType(ir.VoidType(), (a.type.irtype for a in self.args), False)
        typemap[self.name] = self

    def emit(self, module):
        self.func = ir.Function(module, self.irtype, self.name)

    def call(self, builder, stack):
        count = len(self.func.args)
        args = stack[-count:]
        del stack[-count:]
        stack.append(builder.call(self.func, args))

    def __repr__(self):
        args = ', '.join(str(a) for a in self.args) if self.args else ''
        return 'cdecl fn %s(%s)' % (self.name, args)
