from __future__ import annotations

from typing import Generic, TypeVar

from adventofcode2021.utils.abstract import FileReaderSolution
from adventofcode2021.utils.graph import Graph
from adventofcode2021.utils.stack import Stack

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(
        self,
        state: T,
        parent: Node | None,
    ) -> None:
        self.state: T = state
        self.parent: Node | None = parent

    def __repr__(self):
        return repr(self.state)


class Day12:
    g: Graph

    def create_graph(self, input_data: list[str]):
        self.g = Graph()
        for line in input_data:
            start, end = line.split("-")
            self.g.add_edge(start, end)

    def find_paths(self, initial: str) -> int:
        """Find all the paths possible"""
        frontier: Stack = Stack()
        frontier.push(Node(initial, None))

        # Explored is where we have been
        explored = {initial}

        while not frontier.empty:
            current_node = frontier.pop()
            if current_node.state == "end":
                return current_node

            for child in self.g.nodes_from_node(current_node.state):
                if child in explored:
                    continue

                explored.add(child)
                frontier.push(Node(child, current_node))
        return None


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_graph(input_data.splitlines())
        # Find path
        paths = self.find_paths("start")
        return len(paths)


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
