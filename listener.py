
import sys

from llvmlite import ir
from llvmlite import binding

from aevumListener import aevumListener

from typemap import *
from symbols import *
from ast import *

class Listener(aevumListener):
    def __init__(self):
        self.stack = []
        self._mark = []
        self.symboltable = builtins()
        self.module = ir.Module(name="main")
        self.module.triple = binding.get_default_triple()

    def enterStruct_def(self, ctx):
        self.mark()

    def exitStruct_def(self, ctx):
        members = self.cut()
        s = Struct(ctx.Identifier().getText(), {m.name: m for m in members})
        self.stack.append(s)
        self.symboltable[s.name] = s

        print(self.stack, file=sys.stderr)

    def enterVar_decl(self, ctx):
        self.stack.append(VarDecl(ctx.Identifier().getText(), ctx.type_expr().getText()))
        print(self.stack, file=sys.stderr)

    def enterAssignment(self, ctx):
        self.mark()

    def exitAssignment(self, ctx):
        target, value = self.cut()
        assign = Assignment(target, value)
        self.stack.append(assign)
        print("assignment", target, value, file=sys.stderr)

    def enterFunction_args(self, ctx):
        self.mark()

    def exitFunction_args(self, ctx):
        args = self.cut()
        self.stack.append({a.name: a for a in args})
        print(self.stack, file=sys.stderr)

    def exitCdecl(self, ctx):
        args = self.stack.pop()
        name = ctx.function_decl().Identifier().getText()
        func = CFunction(name, args)
        self.stack.append(func)
        self.symboltable[name] = func
        print(self.stack, file=sys.stderr)

    def enterBlock(self, ctx):
        self.mark()

    def exitBlock(self, ctx):
        body = self.cut()
        self.stack.append(list(body))
        print(self.stack, file=sys.stderr)

    def exitFunction_def(self, ctx):
        body = self.stack.pop()
        args = self.stack.pop()
        name = ctx.function_decl().Identifier().getText()
        func = Function(name, args, body, self.symboltable)
        self.stack.append(func)
        self.symboltable[name] = func
        print(self.stack, file=sys.stderr)

    def enterNamed_reference(self, ctx):
        name = ctx.Identifier().getText()
        self.stack.append(Var(name))
        print(self.stack, file=sys.stderr)

    def exitMember_expression(self, ctx):
        target = self.stack.pop()
        name = ctx.Identifier().getText()
        self.stack.append(Member(target, name))
        print(self.stack, file=sys.stderr)

    def enterCall_expression(self, ctx):
        self.mark()

    def exitCall_expression(self, ctx):
        args = self.cut()
        self.stack.append(Call(args[0], args[1:]))
        print(self.stack, file=sys.stderr)

    def enterString_literal(self, ctx):
        self.stack.append(ConstantString(ctx.getText()))

    def enterInteger_literal(self, ctx):
        self.stack.append(ConstantInt(int(ctx.getText())))

    def enterFloating_point_literal(self, ctx):
        self.stack.append(ConstantFloat(float(ctx.getText())))

    def mark(self):
        self._mark.append(len(self.stack))

    def cut(self):
        mark = self._mark.pop()
        data = self.stack[mark:]
        self.stack = self.stack[:mark]
        return data

    def typecheck(self):
        for s in self.stack:
            s.typecheck(self.symboltable)

    def emit(self):
        for s in self.stack:
            s.emit(self.module)
        return str(self.module)
