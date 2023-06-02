from dataclasses import dataclass
from itertools import chain
from typing import Callable


@dataclass(frozen=True)
class Rule:
    output: str
    rule: list[str]


def transitive(accumulator, op: Callable):
    while True:
        # print("acc", accumulator)
        current = op(accumulator)
        if accumulator == current:
            return current
        accumulator = current


class ParseTable:
    def __init__(self, flat_grammar: list[Rule], start: str):
        self.start = start
        self.grammar: dict[str, list[list[str]]] = dict()
        for rule in flat_grammar:
            self.grammar.setdefault(rule.output, []).append(rule.rule)
        self.non_terminals = frozenset(self.grammar.keys())
        self.terminals = frozenset(
            [
                t
                for t in chain.from_iterable([rule.rule for rule in flat_grammar])
                if not t in self.non_terminals
            ]
        )

        print("terminals", self.terminals)
        print("non-terminals", self.non_terminals)

        # setup the FIRST table
        def first_op(accumulator) -> dict[str, set[str]]:
            result: dict[str, set[str]] = dict()
            for k, productions in self.grammar.items():
                for production in productions:
                    if len(production) > 0:
                        p = production[0]
                        if p in accumulator:
                            result.setdefault(k, set()).update(accumulator[p])
                        elif p in self.terminals:
                            result.setdefault(k, set()).add(p)
            return result

        self.first = transitive(dict(), first_op)

        # setup the FOLLOW table
        def follow_op(accumulator) -> dict[str, set[str]]:
            result: dict[str, set[str]] = dict()
            for k, productions in self.grammar.items():
                for production in productions:
                    for i, p in enumerate(production):
                        if not p in self.non_terminals:
                            continue
                        if i + 1 < len(production):
                            q = production[i + 1]
                            if q in self.terminals:
                                result.setdefault(p, set()).add(q)
                            elif q in self.first:
                                result.setdefault(p, set()).update(self.first[q])
                        elif k in accumulator:
                            result.setdefault(p, set()).update(accumulator[k])
            return result

        self.follow = transitive(dict(), follow_op)

        self.m = dict()
        for rule in flat_grammar:
            A = rule.rule
            for a in self.first.get(a, set()):
                if a in self.terminals:
                    self.m.setdefault((A, a), set()).add(rule)
                if 


        print("first", self.first)
        print("follow", self.follow)

def parse(table, input):
    pass

if __name__ == "__main__":
    grammar = [
        Rule("module", ["struct_p"]),
        Rule("module", ["module", "module"]),
        Rule("module", []),
        Rule("struct_p", ["struct", "ident", "{", "field_list", "}"]),
        Rule("field_list", ["field"]),
        Rule("field_list", ["field_list", ",", "field_list"]),
        Rule("field", ["ident", ":", "ident"]),
    ]

    table = ParseTable(grammar, "module")

    input = """
    struct ident { ident : ident }
    """

    print(input.split())

    result = parse(table, input.split())
    print(result)
