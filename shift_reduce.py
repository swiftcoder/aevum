from dataclasses import dataclass
from functools import reduce
from itertools import chain, pairwise
from typing import Callable, Iterable, Tuple

from more_itertools import nth
from lexer import Token, TokenType


class Matcher:
    def __call__(self, _):
        pass


@dataclass(frozen=True)
class Rule:
    output: Matcher
    rule: list[Matcher]


@dataclass(frozen=True)
class Position:
    output: Matcher
    rule: list[Matcher]
    offset: int = 0
    lookahead: frozenset[Matcher] = frozenset()


def transitive(accumulator, op: Callable):
    while True:
        # print("acc", accumulator)
        current = op(accumulator)
        if accumulator == current:
            return current
        accumulator = current


class ParseTable:
    def __init__(self, flat_grammar: list[Rule], start: str):
        self.grammar: dict[Matcher, list[list[Matcher]]] = dict()
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
        def first_op(accumulator) -> dict[Matcher, set[Matcher]]:
            result: dict[Matcher, set[Matcher]] = dict()
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
        def follow_op(accumulator) -> dict[Matcher, set[Matcher]]:
            result: dict[Matcher, set[Matcher]] = dict()
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

        print("first", self.first)
        print("follow", self.follow)

    def get_first(self, p: Matcher) -> set[Matcher]:
        return self.first.get(p, set([p]))

    def get_state(self, p: Position) -> set[Position]:
        result: dict[Tuple[Matcher, list[Matcher], int], set[Matcher]] = dict()

        current = p.rule[p.offset]
        if current in self.non_terminals:
            if p.offset + 1 < len(p.rule):
                lookahead = self.get_first(p.rule[p.offset + 1])
            else:
                lookahead = self.follow[p.output]
            for rule in self.grammar[current]:
                result.setdefault((current, rule, 0), set()).update(lookahead)

        return set(
            [
                Position(output, rule, offset, frozenset(lookahead))
                for (output, rule, offset), lookahead in result.items()
            ]
        )

    def get_goto(self, state: set[Position]):
        pass

    def get_action(self, state: set[Position], input: Token):
        pass


def parse(tokens: list[Token]):
    grammar = [
        Rule(
            rule("struct"),
            [keyword("struct"), ident(), punct("{"), rule("field_list"), punct("}")],
        ),
        Rule(rule("field"), [ident(), punct(":"), ident()]),
        Rule(
            rule("field_list"),
            [rule("field_list"), punct(","), rule("field_list")],
        ),
        Rule(
            rule("field_list"),
            [rule("field")],
        ),
    ]
    start = "struct"

    table = ParseTable(grammar, start)

    def _reduce(stack) -> bool:
        for rule in grammar:
            non_terminal = rule.output
            production = rule.rule

            # print(f"applying rule {production} -> {non_terminal}")
            result = [p(n) for p, n in zip(production, stack[-len(production) :])]
            if len(result) == len(production) and all(result):
                print(f"reducing {stack[-len(production):]} to {non_terminal}")
                del stack[-len(production) :]
                stack.append(non_terminal)
                return True
        return False

    state : set[Position] = set()
    stack: list[Token | Matcher] = []
    while tokens or len(stack) > 1:
        print("stack", stack)
        if _reduce(stack):
            continue
        if tokens:
            stack.append(tokens.pop(0))  # Shift

    return len(stack) == 1 and stack[0] == rule(start)


@dataclass(frozen=True)
class keyword(Matcher):
    value: str

    def __call__(self, token):
        return (
            isinstance(token, Token)
            and token.type == TokenType.Keyword
            and token.value == self.value,
        )


@dataclass(frozen=True)
class ident(Matcher):
    def __call__(self, token):
        return (isinstance(token, Token) and token.type == TokenType.Ident,)


@dataclass(frozen=True)
class punct(Matcher):
    value: str

    def __call__(self, token):
        return (
            isinstance(token, Token)
            and token.type == TokenType.Punctuation
            and token.value == self.value
        )


@dataclass(frozen=True)
class rule(Matcher):
    name: str

    def __call__(self, token):
        return token == self or (isinstance(token, str) and token == self.name)


if __name__ == "__main__":
    grammar = {"S": [["S", "+", "S"], ["S", "*", "S"], ["id"]]}

    class ShiftReduceParser:
        def __init__(self, grammar):
            self.grammar = grammar

        def parse(self, input_tokens):
            stack = []
            while input_tokens or stack:
                print(stack)
                if self.reduce(stack):
                    continue
                if not input_tokens:
                    return False  # Parsing failed
                stack.append(input_tokens.pop(0))  # Shift
            return True  # Parsing succeeded

        def reduce(self, stack) -> bool:
            for non_terminal, productions in self.grammar.items():
                for production in productions:
                    if stack[-len(production) :] == production:
                        del stack[-len(production) :]
                        stack.append(non_terminal)
                        return True
            return False

    parser = ShiftReduceParser(grammar)
    print(parser.parse(["id", "+", "id", "*", "id"]))  # Should print: True
    # print(parser.parse(['id', '+', '+', 'id']))  # Should print: False
