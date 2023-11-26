from __future__ import annotations

from adventofcodeutils.graph import Graph
from adventofcodeutils.node import Node
from adventofcodeutils.stack import Stack

from adventofcode.utils.abstract import FileReaderSolution


class Day12:
    g: Graph

    def create_graph(self, input_data: list[str]):
        self.g = Graph()
        for line in input_data:
            start, end = line.split("-")
            self.g.add_edge(start, end)

    def find_paths(self, initial: str, max_visits: int = 1) -> list[Node]:
        """Find all the paths possible"""
        frontier: Stack = Stack()
        frontier.push(Node(initial, None))

        # Explored is where we have been
        paths = []

        while not frontier.empty:
            current_node = frontier.pop()
            if current_node.state == "end":
                paths.append(current_node)
                continue

            for child in self.g.nodes_from_node(current_node.state):
                if child == "start":
                    # We can visit start only once
                    continue
                elif child.isupper():
                    # Uppercase, we can visit this node mode
                    pass
                else:
                    # We can visit a lowercase node only once
                    visited_list = Node.node_to_path(current_node)
                    if max_visits == 2:
                        lower_cases = [node for node in visited_list if node.islower()]
                        unique_lower = set(lower_cases)
                        if len(lower_cases) == len(unique_lower) + 2:
                            continue
                    else:
                        if visited_list.count(child) >= max_visits:
                            continue

                frontier.push(Node(child, current_node))
        return paths


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_graph(input_data.splitlines())
        # Find path
        paths = self.find_paths("start", 1)
        return len(paths)


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_graph(input_data.splitlines())
        # Find path
        paths = self.find_paths("start", 2)
        return len(paths)
