
class SymbolNotFound(Exception):
    pass

class SymbolTable(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.table = {}

    def __getitem__(self, index):
        symbol = self.table.get(index) or (self.parent[index] if self.parent else None)
        if not symbol:
            raise SymbolNotFound(index)
        return symbol

    def __setitem__(self, index, value):
        self.table[index] = value

    def __str__(self):
        return self.table.__str__()
