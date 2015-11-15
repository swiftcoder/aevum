
class SymbolTable(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.table = {}

    def __getitem__(self, index):
        return self.table.get(index) or self.parent[index]

    def __setitem__(self, index, value):
        self.table[index] = value

    def __str__(self):
        return self.table.__str__()
