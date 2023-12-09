from __future__ import annotations

import logging
import math
import re
from itertools import cycle

from adventofcode.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


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
        match = re.compile(r"[A-Z\d]{3}")
        self.nodes = {}

        for line in input_data.splitlines():
            parts = re.findall(match, line)
            self.nodes[parts[0]] = parts[1:]

    def find_cycle(self, start_node: str) -> int:
        steps = 0
        current_node = start_node

        for instruction in cycle(self.instructions):
            steps += 1
            if instruction == "L":
                current_node = self.nodes[current_node][0]
            else:
                current_node = self.nodes[current_node][1]
            if current_node.endswith("Z"):
                return steps


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.find_cycle("AAA")


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)

        starts = [node for node in self.nodes.keys() if node[2] == "A"]
        logger.info("We have %s starts", len(starts))

        return math.lcm(*(self.find_cycle(start) for start in starts))
