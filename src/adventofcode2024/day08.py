from __future__ import annotations

import itertools
import logging
from typing import Optional

import attrs

from adventofcode.utils.abstract import FileReaderSolution

_logger = logging.getLogger(__name__)


@attrs.define(order=True)
class Node:
    value: str
    row: int = attrs.field(order=True)
    column: int = attrs.field(order=True)
    is_antinode: bool = False
    original_antenna: str | None = attrs.field(default=False, eq=False, order=False)


class Day08:
    max_row: int
    max_col: int

    @staticmethod
    def map_to_nodes(input_lines: str) -> list[Node]:
        nodes = []
        for row, line in enumerate(input_lines.splitlines()):
            for column, char in enumerate(line):
                if char != ".":
                    nodes.append(
                        Node(
                            value=char,
                            row=row,
                            column=column,
                            is_antinode=True if char == "#" else False,
                        )
                    )
        return nodes


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        nodes = self.map_to_nodes(input_data)
        self.max_col = len(input_data.splitlines())
        self.max_row = len(input_data.splitlines()[0])
        _logger.debug(f"Found max_row: {self.max_row}, max_col: {self.max_col}")

        anti_nodes = self.find_antinodes_in_group(nodes)
        return len(anti_nodes)

    def find_antinodes_in_group(self, nodes: list[Node]) -> list[Node]:
        """Find the antinodes from the list of nodes"""
        antinodes = []
        node_points: set[tuple[int, int]] = {(node.row, node.column) for node in nodes}
        for group in {node.value for node in nodes}:
            nodes_in_group = [node for node in nodes if node.value == group]
            antinodes.extend(self.find_antinodes(nodes_in_group, node_points))
        return antinodes

    def find_antinodes(
        self,
        nodes: list[Node],
        node_points: set[tuple[int, int]],
    ) -> list[Node]:
        """Find all antinodes from the list of nodes for a specific antenna"""
        if not nodes:
            return []

        antinodes = []
        for x, y in itertools.permutations(nodes, 2):
            delta_row = x.row - y.row
            delta_col = x.column - y.column
            new_row = x.row + delta_row
            new_col = x.column + delta_col
            if 0 <= new_row <= self.max_row and 0 <= new_col <= self.max_col:
                antinode = Node(
                    value="#",
                    row=new_row,
                    column=new_col,
                    is_antinode=True,
                    original_antenna=x.value,
                )
                if (new_row, new_col) in node_points:
                    _logger.debug(f"Found antinode: {antinode} already occupied")
                    continue

                antinodes.append(antinode)

        return antinodes


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return -2
