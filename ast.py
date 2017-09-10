
import sys

from llvmlite import ir

from symbols import *
import type
import names

next_serial = 1

class NoMatchingFunctionSignature(Exception):
    pass

class NotAllArrayMembersOfSameType(Exception):
    pass

class AST(object):
    def __init__(self, **args):
        self._dependencies = args.get('dependencies', [])
        self._internal_dependencies = args.get('internal_dependencies', [])
        self._has_symbol_table = args.get('has_symbol_table', False)
        self._symbols = args.get('symbols', [])
        self._populate_symbols = args.get('populate_symbols', [])
        self._lookup_one = args.get('lookup_one', [])
        self._lookup_many = args.get('lookup_many', [])

    def populate_symbol_table(self, symboltable):
        for name, symbol in self._symbols:
            symboltable.put(name, symbol)

        if self._has_symbol_table:
            symboltable = SymbolTable(symboltable)
            self.symboltable = symboltable

        for p in self._populate_symbols:
            p.populate_symbol_table(symboltable)

    def dependent_types(self, symboltable):
        deps = []
        direct = []
        for d in self._dependencies:
            deps += d.dependent_types(symboltable)
        if self._has_symbol_table:
            for i in self._internal_dependencies:
                deps += i.dependent_types(self.symboltable)
        for field, name in self._lookup_one:
            item = symboltable.match_one(name)
            setattr(self, field, item)
            direct += [item]
        for field, name in self._lookup_many:
            items = symboltable.match(name)
            setattr(self, field, items)
            direct += items
        return [(self, self._dependencies + direct)] + deps

    def typecheck(self, symboltable):
        pass

    def typecheck_body(self, symboltable):
        pass

    def emit(self, module):
        pass

class Type(AST):
    def __init__(self, name):
        super().__init__(lookup_one=[('type', name)])
        self.name = name

class ArrayType(AST):
    def __init__(self, inner):
        super().__init__(dependencies=[inner])
        self.inner = inner
        self.name = 'array_of_' + inner.name

    def typecheck(self, symboltable):
        self.inner.typecheck(symboltable)
        self.type = type.ArrayType(self.inner.type)

class Void(AST):
    def __init__(self):
        super().__init__()
        self.type = type.VoidType

class ConstantBool(AST):
    def __init__(self, value):
        super().__init__()
        self.value = bool(value)
        self.type = type.BoolType

    def emit(self, builder, stack):
        i = ir.Constant(ir.IntType(1), self.value)
        stack.append(i)

    def __repr__(self):
        return 'bool %s' % (self.value)

class ConstantString(AST):
    def __init__(self, data):
        super().__init__()
        data = data[1:-1]
        self.data = data.replace('\\\"', '\"') + '\0'
        self.type = type.StringType

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
        super().__init__(dependencies=elements)
        self.elements = elements
        self.type = None

    def typecheck(self, symboltable):
        if len(self.elements) > 0:
            self.innerType = self.elements[0].type
            for e in self.elements:
                if e.type != self.innerType:
                    raise NotAllArrayMembersOfSameType()
            self.type = type.ArrayType(self.innerType)

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
        super().__init__()
        self.value = int(value)
        self.type = type.Int32Type

    def emit(self, builder, stack):
        i = ir.Constant(ir.IntType(32), self.value)
        stack.append(i)

    def __repr__(self):
        return 'int %s' % (self.value)

class ConstantFloat(AST):
    def __init__(self, value):
        super().__init__()
        if value.startswith('0x') or value.startswith('0X'):
            self.value = float.fromhex(value)
        else:
            self.value = float(value)
        self.type = type.FloatType

    def emit(self, builder, stack):
        i = ir.Constant(ir.FloatType(), self.value)
        stack.append(i)

    def __repr__(self):
        return 'float %s' % (self.value)

class VarRef(AST):
    def __init__(self, name):
        super().__init__(lookup_one=[('item', name)])
        self.name = name

    def typecheck(self, symboltable):
        if hasattr(self, 'item') and hasattr(self.item, 'type'):
            self.type = self.item.type

    def emit(self, builder, stack):
        self.item.fetch(builder, stack)

    def reference(self, builder):
        return self.item.reference(builder)

    def as_function_ref(self, args):
        return FunctionRef(self.name, args)

    def __repr__(self):
        return 'varref %s' % (self.name)

class FunctionRef(AST):
    def __init__(self, name, args):
        super().__init__(dependencies=args, lookup_many=[('items', name)])
        self.name = name
        self.args = args

    def typecheck(self, symboltable):
        args = [a.type for a in self.args]
        for i in self.items:
            if len(i.args) == len(args) and all(a.type == b for a, b in zip(i.args, args)):
                self.item = i
                return
        raise NoMatchingFunctionSignature(self.name, self.items, self.args)

    def emit(self, builder, stack):
        self.item.fetch(builder, stack)

    def call(self, builder, stack):
        self.item.call(builder, stack)

    def __repr__(self):
        return 'funcref %s' % (self.name)

class Member(AST):
    def __init__(self, target, name):
        super().__init__(dependencies=[target])
        self.target = target
        self.name = name

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
        self.func = func.as_function_ref(args)
        super().__init__(dependencies=[self.func])
        self.args = args

    def typecheck(self, symboltable):
        for a in self.args:
            a.typecheck(symboltable)
        self.func.typecheck(symboltable)

    def emit(self, builder, stack):
        for a in self.args:
            a.emit(builder, stack)
        self.func.call(builder, stack)

    def __repr__(self):
        args = ', '.join(str(a) for a in self.args) if self.args else ''
        return 'call %s(%s)' % (str(self.func), args)

class VarDecl(AST):
    def __init__(self, name, typeexpr):
        super().__init__(dependencies=[typeexpr], symbols=[(name, self)])
        self.name = name
        self.typeexpr = typeexpr

    def typecheck(self, symboltable):
        self.typeexpr.typecheck(symboltable)
        self.type = self.typeexpr.type

    def emit(self, builder, stack):
        self.item = builder.alloca(self.type.irtype)
        stack.append(builder.load(self.item))

    def fetch(self, builder, stack):
        stack.append(builder.load(self.item))

    def reference(self, builder):
        return self.item

    def __repr__(self):
        return '%s : %s' % (self.name, self.typeexpr)

class Assignment(AST):
    def __init__(self, target, value):
        super().__init__(dependencies=[target, value])
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

class Struct(AST):
    def __init__(self, name, members):
        super().__init__(dependencies=members, symbols=[(name, self)])
        self.name = name
        self._members = members
        self.members = {m.name: m for m in self._members}

    def typecheck(self, symboltable):
        for m in self._members:
            m.typecheck(symboltable)

        self.irtype = ir.context.global_context.get_identified_type(self.name)
        self.irtype.set_body(*[m.type.irtype for m in self._members])
        self.type = type.StructType(self.name, {m.name: m.type for m in self._members}, self.irtype)

    def __repr__(self):
        members = ', '.join(str(s) for s in self._members) if self._members else ''
        return 'struct %s {%s}' % (self.name, members)

class BaseFunction(AST):
    def typecheck(self, symboltable):
        for a in self.args:
            a.typecheck(symboltable)

        self.irtype = ir.FunctionType(self.result.type.irtype, (a.type.irtype for a in self.args), False)

    def emit(self, module):
        self.func = ir.Function(module, self.irtype, self.name())

    def call(self, builder, stack):
        count = len(self.func.args)
        if count > 0:
            args = stack[-count:]
            del stack[-count:]
        else:
            args = []
        stack.append(builder.call(self.func, args))

class Function(BaseFunction):
    def __init__(self, name, args, result, body):
        super().__init__(dependencies=[result] + args, internal_dependencies=body, has_symbol_table=True, symbols=[(name, self)], populate_symbols=args + body)
        self._name = name
        self.args = args
        self.body = body
        self.result = result

    def typecheck(self, symboltable):
        super().typecheck(symboltable)

        for a in self.args:
            self.symboltable.put(a.name, a)

    def typecheck_body(self, symboltable):
        for b in self.body:
            b.typecheck(self.symboltable)

    def emit(self, module):
        super().emit(module)

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

    def name(self):
        return names.mangle(self._name, [a.type.name for a in self.args])

    def __repr__(self):
        args = ', '.join(str(a) for a in self.args) if self.args else ''
        body = '; '.join(str(s) for s in self.body) + ';' if self.body else ''
        return 'fn %s(%s) {%s}' % (self._name, args, body)

class CFunction(BaseFunction):
    def __init__(self, name, args, result):
        super().__init__(dependencies=[result] + args, symbols=[(name, self)])
        self._name = name
        self.args = args
        self.result = result

    def name(self):
        return self._name

    def __repr__(self):
        args = ', '.join(str(a) for a in self.args) if self.args else ''
        return 'cdecl fn %s(%s)' % (self._name, args)

class If(AST):
    def __init__(self, expr, block_then, block_else=[]):
        super().__init__(dependencies=[expr], internal_dependencies=block_then + block_else, has_symbol_table=True, populate_symbols=[expr] + block_then + block_else)
        self.expr = expr
        self.block_then = block_then
        self.block_else = block_else

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

def comparison(op, lhs, rhs):
    name = {
        '==': '__eq__',
        '!=': '__neq__'
    }[op]
    return Call(VarRef(name), [lhs, rhs])
