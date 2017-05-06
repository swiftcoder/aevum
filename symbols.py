
class SymbolNotFound(Exception):
    pass

class SymbolConflict(Exception):
    pass

class SymbolTable(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.table = {}

    def put(self, key, item):
        self.table.setdefault(key, []).append(item)

    def match(self, key):
        result = self.table.get(key, [])
        if self.parent:
            result += self.parent.match(key)
        return result

    def match_one(self, key):
        result = self.table.get(key, [])
        if len(result) > 1:
            raise SymbolConflict(key)
        if len(result) == 0 and self.parent:
            return self.parent.match_one(key)
        return result[0]

    def __str__(self):
        return self.table.__str__()
