from __future__ import annotations

from collections import Counter
from typing import Generic, TypeVar

import tqdm

from adventofcode2021.utils.abstract import FileReaderSolution

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


class Day14(Generic[T]):
    root_node: Polymer

    def initialize(self, input_data: str):
        lines = input_data.splitlines()
        self.parse_template(lines[0])
        self.parse_rules(lines[2:])

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

    def parse_rules(self, rules: list[str]):
        self.rules: dict[str, str] = {}
        for rule in rules:
            pair = rule.split(" -> ")
            self.rules[pair[0]] = pair[1]

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


class Day14PartA(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.initialize(input_data)
        for _ in range(10):
            self.step()
        return self.count()


class Day14PartB(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.initialize(input_data)
        for _ in tqdm.trange(40):
            self.step()
        return self.count()
