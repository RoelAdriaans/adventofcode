from __future__ import annotations

import attrs
from adventofcodeutils.parsing import extract_digits_from_string

from adventofcode.utils.abstract import FileReaderSolution


@attrs.define
class Node:
    name: str

    size: int
    used: int
    avail: int

    x: int
    y: int

    @classmethod
    def from_string(cls, string: str) -> Node:
        """Parse a line into a Node:
        Filesystem              Size  Used  Avail  Use%
        /dev/grid/node-x0-y4     94T   73T    21T   77%
        """
        items = extract_digits_from_string(string)
        name = string.split()[0]
        nd = cls(
            name, size=items[2], used=items[3], avail=items[4], x=items[0], y=items[1]
        )
        return nd


class Day22:
    def parse(self, input_data: str) -> list[Node]:
        return [Node.from_string(line) for line in input_data.splitlines()[2:]]


class Day22PartA(Day22, FileReaderSolution):
    @staticmethod
    def find_pairs(nodes: list[Node]) -> int:
        found = 0
        for node in nodes:
            if node.used == 0:
                continue
            for test_node in nodes:
                if node.name == test_node.name:
                    continue
                if test_node.avail >= node.used:
                    found += 1

        return found

    def solve(self, input_data: str) -> int:
        nodes = self.parse(input_data)
        res = self.find_pairs(nodes)
        return res


class Day22PartB(Day22, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
