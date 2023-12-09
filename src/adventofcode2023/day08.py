from __future__ import annotations

import re
from itertools import cycle

from adventofcode.utils.abstract import FileReaderSolution


class Day08:
    instructions: str
    nodes: dict[str, list[str]]

    def parse(self, input_data: str):
        instructions, nodes = input_data.split("\n\n")
        self.instructions = instructions

        self.parse_nodes(nodes)

    def parse_nodes(self, input_data: str):
        """Parse a line with into parts, and add to the nodes dict
        Format must be: VRN = (CSM, GPD)"""
        match = re.compile(r"[A-Z]{3}")
        self.nodes = {}

        for line in input_data.splitlines():
            parts = re.findall(match, line)
            self.nodes[parts[0]] = parts[1:]


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        steps = 0
        current_node = "AAA"
        instructions = cycle(self.instructions)

        while current_node != "ZZZ":
            instruction = next(instructions)
            if instruction == "L":
                current_node = self.nodes[current_node][0]
            else:
                current_node = self.nodes[current_node][1]
            steps += 1

        return steps


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
