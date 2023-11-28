from __future__ import annotations

from abc import ABC, abstractmethod
from collections import Counter
from typing import Generic, TypeVar

from adventofcode.utils.abstract import FileReaderSolution

T = TypeVar("T")


class Polymer(Generic[T]):
    child: Polymer | None = None

    def __init__(self, polymer: T, parent: Polymer | None = None):
        """
        Create a new Polymer with type T.

        If parent is given, this Polymer adds itself to this parent as child
        """
        self._content = polymer
        if parent:
            parent.add_child(self)

    def add_child(self, child: Polymer):
        if self.child is None:
            self.child = child
        else:
            raise ValueError(
                f"Polymer {self._content} already has a child {self.child}"
            )

    @property
    def content(self) -> T:
        return self._content

    def __repr__(self):
        return repr(self._content)


class Day14(ABC):
    def initialize(self, input_data: str):
        lines = input_data.splitlines()
        self.parse_template(lines[0])
        self.parse_rules(lines[2:])

    @abstractmethod
    def parse_template(self, template: str):
        raise NotImplementedError

    def parse_rules(self, rules: list[str]):
        self.rules: dict[str, str] = {}

        for rule in rules:
            pair = rule.split(" -> ")
            self.rules[pair[0]] = pair[1]


class Day14PartA(Day14, FileReaderSolution, Generic[T]):
    root_node: Polymer

    def polimers_to_list(self) -> list[str]:
        path: list[str] = [self.root_node.content]
        node = self.root_node

        while node.child is not None:
            node = node.child
            path.append(node.content)

        return path

    def parse_template(self, template: str):
        self.root_node = Polymer(template[0])
        current = self.root_node
        for element in template[1:]:
            current = Polymer(element, current)

    def step(self):
        """Apply the rules to the polymers"""
        current_node = self.root_node
        while current_node.child:
            next_node = current_node.child
            pair = f"{current_node.content}{next_node.content}"
            element_to_add = self.rules[pair]

            # Add a new polymer and add it between current_node and it's child
            new_polymer = Polymer(element_to_add)
            current_node.child = new_polymer
            new_polymer.child = next_node
            # And go to the next node in the chain
            current_node = next_node

    def count(self) -> int:
        chain = self.polimers_to_list()
        cnt = Counter(chain)
        common = cnt.most_common()
        return common[0][1] - common[-1][1]

    def solve(self, input_data: str) -> int:
        self.initialize(input_data)
        for _ in range(10):
            self.step()
        return self.count()


class Day14PartB(Day14, FileReaderSolution):
    cnt: Counter[str]
    word_counter: Counter[str]

    def parse_template(self, template: str):
        self.cnt = Counter()
        for step in range(0, len(template) - 1):
            self.cnt[template[step : step + 2]] += 1

    def step(self):
        new_counter: Counter[str] = Counter()
        self.word_counter = Counter()
        for item, count in self.cnt.items():
            new_polymer = self.rules[item]
            left = f"{item[0]}{new_polymer}"
            right = f"{new_polymer}{item[1]}"
            new_counter[left] += count
            new_counter[right] += count

            self.word_counter[item[0]] += count
            self.word_counter[new_polymer] += count

        self.cnt = new_counter

    def count(self, char_to_fix: str) -> int:
        # Fix off by one error for the last character in the recipe
        self.word_counter[char_to_fix] += 1
        common = self.word_counter.most_common()
        return common[0][1] - common[-1][1]

    def solve(self, input_data: str) -> int:
        self.initialize(input_data)
        self.word_counter = Counter()
        for _ in range(40):
            self.step()
        char_to_fix = input_data.splitlines()[0][-1]
        return self.count(char_to_fix)
