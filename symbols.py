
# handles symbol lookup in nested scopes
class SymbolTable:
    def __init__(self):
        self.table = [dict()]

    def push_scope(self):
        self.table.append(dict())

    def pop_scope(self):
        if len(self.table) < 2:
            raise Exception("attempted to pop the global scope")
        self.table.pop()

    def define(self, name, value):
        self.table[-1][name] = value

    def lookup(self, name):
        # print(f"looking up {name}")
        for i in range(len(self.table) - 1, -1, -1):
            if name in self.table[i]:
                return self.table[i][name]
