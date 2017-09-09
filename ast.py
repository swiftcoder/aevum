
import sys

from llvmlite import ir

from symbols import *
from typemap import *
import names

next_serial = 1

class NoMatchingFunctionSignature(Exception):
    pass

class NotAllArrayMembersOfSameType(Exception):
    pass

class AST(object):
    def populate_symbol_table(self, symboltable):
        pass

    def dependent_types(self, symboltable):
        return [(self, [])]

    def typecheck(self, symboltable):
        pass

class ConstantBool(AST):
    def __init__(self, value):
        self.value = bool(value)
        self.type = BoolType

    def emit(self, builder, stack):
        i = ir.Constant(ir.IntType(1), self.value)
        stack.append(i)

    def __repr__(self):
        return 'bool %s' % (self.value)

class ConstantString(AST):
    def __init__(self, data):
        data = data[1:-1]
        self.data = data.replace('\\\"', '\"') + '\0'
        self.type = StringType

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

class ConstantArray(AST):
    def __init__(self, elements):
        self.elements = elements
        self.type = None

    def dependent_types(self, symboltable):
        dependencies = []
        for e in self.elements:
            dependencies += e.dependent_types(symboltable)
        return [(self, self.elements)] + dependencies

    def typecheck(self, symboltable):
        if len(self.elements) > 0:
            self.innerType = self.elements[0].type
            for e in self.elements:
                if e.type != self.innerType:
                    raise NotAllArrayMembersOfSameType()
            self.type = ArrayType(self.innerType)

    def emit(self, builder, stack):
        global next_serial
        aname = 'array_inner_constant_%d' % (next_serial)
        name = 'array_constant_%d' % (next_serial)
        next_serial += 1

        for e in self.elements:
            e.emit(builder, stack)

        count = len(self.elements)
        elements = stack[-count:]
        del stack[-count:]

        ta = ir.ArrayType(self.innerType.irtype, count)
        globa = ir.GlobalVariable(builder.module, ta, name=aname)
        globa.global_constant = True
        globa.initializer = ir.Constant(ta, elements)
        z = ir.Constant(ir.IntType(32), 0)
        ga = globa.gep([z, z])

        c = ir.Constant(ir.IntType(32), count)

        glob = ir.GlobalVariable(builder.module, self.type.irtype, name=name)
        glob.global_constant = True
        glob.initializer = ir.Constant.literal_struct([c, ga])
        stack.append(builder.load(glob))

    def __repr__(self):
        return 'array [%s]' % (', '.join(str(e) for e in self.elements))

class ConstantInt(AST):
    def __init__(self, value):
        self.value = int(value)
        self.type = Int32Type

    def emit(self, builder, stack):
        i = ir.Constant(ir.IntType(32), self.value)
        stack.append(i)

    def __repr__(self):
        return 'int %s' % (self.value)

class ConstantFloat(AST):
    def __init__(self, value):
        if value.startswith('0x') or value.startswith('0X'):
            self.value = float.fromhex(value)
        else:
            self.value = float(value)
        self.type = FloatType

    def emit(self, builder, stack):
        i = ir.Constant(ir.FloatType(), self.value)
        stack.append(i)

    def __repr__(self):
        return 'float %s' % (self.value)

class VarRef(AST):
    def __init__(self, name):
        self.name = name

    def dependent_types(self, symboltable):
        self.item = symboltable.match_one(self.name)
        return [(self, [self.item])]

    def dependent_types_func(self, symboltable):
        self.items = symboltable.match(self.name)
        return [(self, self.items)]

    def typecheck(self, symboltable):
        if hasattr(self, 'item') and hasattr(self.item, 'type'):
            self.type = self.item.type

    def typecheck_func(self, symboltable, args):
        for i in self.items:
            if len(i.args) == len(args) and all(a.type == b for a, b in zip(i.args, args)):
                self.item = i
                return
        raise NoMatchingFunctionSignature(self.name, self.items, args)

    def emit(self, builder, stack):
        self.item.fetch(builder, stack)

    def call(self, builder, stack):
        self.item.call(builder, stack)

    def reference(self, builder):
        return self.item.reference(builder)

    def __repr__(self):
        return 'varref %s' % (self.name)

class Member(AST):
    def __init__(self, target, name):
        self.target = target
        self.name = name

    def dependent_types(self, symboltable):
        target_deps = self.target.dependent_types(symboltable)
        return [(self, [self.target])] + target_deps

    def typecheck(self, symboltable):
        self.target.typecheck(symboltable)
        self.type = self.target.item.type.members[self.name].type
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

class Call(AST):
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def dependent_types(self, symboltable):
        dependancies = self.func.dependent_types_func(symboltable)
        for a in self.args:
            dependancies += a.dependent_types(symboltable)
        return [(self, self.args)] + dependancies

    def typecheck(self, symboltable):
        for a in self.args:
            a.typecheck(symboltable)
        self.func.typecheck_func(symboltable, [a.type for a in self.args])

    def emit(self, builder, stack):
        for a in self.args:
            a.emit(builder, stack)
        self.func.call(builder, stack)

    def __repr__(self):
        args = ', '.join(str(a) for a in self.args) if self.args else ''
        return '%s(%s)' % (str(self.func), args)

class VarDecl(AST):
    def __init__(self, name, typename):
        self.name = name
        self.typename = typename

    def populate_symbol_table(self, symboltable):
        symboltable.put(self.name, self)

    def dependent_types(self, symboltable):
        if isinstance(self.typename, list):
            innerType = symboltable.match_one(self.typename[0])
            self.type = ArrayType(innerType)
            self.typename = str(self.type)
            return [(self, [])]
        self.type = symboltable.match_one(self.typename)
        return [(self, [self.type])]

    def emit(self, builder, stack):
        self.item = builder.alloca(self.type.irtype)
        stack.append(builder.load(self.item))

    def fetch(self, builder, stack):
        stack.append(builder.load(self.item))

    def reference(self, builder):
        return self.item

    def __repr__(self):
        return '%s : %s' % (self.name, self.typename)

class Assignment(AST):
    def __init__(self, target, value):
        self.target = target
        self.value = value

    def dependent_types(self, symboltable):
        dependencies = self.target.dependent_types(symboltable)
        dependencies += self.value.dependent_types(symboltable)
        return [(self, [self.target, self.value])] + dependencies

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

class Struct(AST):
    def __init__(self, name, members):
        self.name = name
        self._members = members
        self.members = {m.name: m for m in self._members}

    def populate_symbol_table(self, symboltable):
        symboltable.put(self.name, self)

    def dependent_types(self, symboltable):
        dependencies = []
        for m in self._members:
            dependencies += m.dependent_types(symboltable)
        return [(self, self._members)] + dependencies

    def typecheck(self, symboltable):
        for m in self._members:
            m.typecheck(symboltable)

        self.irtype = ir.LiteralStructType(m.type.irtype for m in self._members)
        self.type = StructType(self.name, {m.name: m.type for m in self._members}, self.irtype)

    def emit(self, module):
        pass

    def __repr__(self):
        members = ', '.join(str(s) for s in self._members) if self._members else ''
        return 'struct %s {%s}' % (self.name, members)

class Function(AST):
    def __init__(self, name, args, body):
        self.name = name
        self.args = args
        self.body = body

    def populate_symbol_table(self, symboltable):
        symboltable.put(self.name, self)

        self.symboltable = SymbolTable(symboltable)
        for a in self.args:
            a.populate_symbol_table(self.symboltable)
        for b in self.body:
            b.populate_symbol_table(self.symboltable)

    def dependent_types(self, symboltable):
        dependencies = []
        for a in self.args:
            dependencies += a.dependent_types(symboltable)
        for b in self.body:
            dependencies += b.dependent_types(self.symboltable)
        return [(self, self.args)] + dependencies

    def typecheck(self, symboltable):
        for a in self.args:
            a.typecheck(symboltable)
            self.symboltable.put(a.name, a)

        for b in self.body:
            b.typecheck(self.symboltable)

        self.irtype = ir.FunctionType(ir.VoidType(), (a.type.irtype for a in self.args), False)

    def emit(self, module):
        self.func = ir.Function(module, self.irtype, self._mangle())
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

    def _mangle(self):
        return names.mangle(self.name, [a.typename for a in self.args])

    def __repr__(self):
        args = ', '.join(str(a) for a in self.args) if self.args else ''
        body = '; '.join(str(s) for s in self.body) + ';' if self.body else ''
        return 'fn %s(%s) {%s}' % (self.name, args, body)

class CFunction(AST):
    def __init__(self, name, args):
        self.name = name
        self.args = args

    def populate_symbol_table(self, symboltable):
        symboltable.put(self.name, self)

    def dependent_types(self, symboltable):
        dependencies = []
        for a in self.args:
            dependencies += a.dependent_types(symboltable)
        return [(self, self.args)] + dependencies

    def typecheck(self, symboltable):
        for a in self.args:
            a.typecheck(symboltable)

        self.irtype = ir.FunctionType(ir.VoidType(), (a.type.irtype for a in self.args), False)

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

class If(AST):
    def __init__(self, expr, block_then, block_else=[]):
        self.expr = expr
        self.block_then = block_then
        self.block_else = block_else

    def populate_symbol_table(self, symboltable):
        self.symboltable = SymbolTable(symboltable)

        self.expr.populate_symbol_table(self.symboltable)
        for b in self.block_then:
            b.populate_symbol_table(self.symboltable)
        for b in self.block_else:
            b.populate_symbol_table(self.symboltable)

    def dependent_types(self, symboltable):
        dependencies = self.expr.dependent_types(self.symboltable)
        for b in self.block_then:
            dependencies += b.dependent_types(self.symboltable)
        for b in self.block_else:
            dependencies += b.dependent_types(self.symboltable)
        return dependencies

    def typecheck(self, symboltable):
        self.expr.typecheck(self.symboltable)
        for b in self.block_then:
            b.typecheck(self.symboltable)
        for b in self.block_else:
            b.typecheck(self.symboltable)

    def emit(self, builder, stack):
        self.expr.emit(builder, stack)
        predicate = stack.pop()
        with builder.if_else(predicate) as (then, otherwise):
            with then:
                for b in self.block_then:
                    b.emit(builder, stack)
            with otherwise:
                for b in self.block_else:
                    b.emit(builder, stack)
