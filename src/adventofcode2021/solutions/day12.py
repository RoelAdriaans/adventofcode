from adventofcode2021.utils.abstract import FileReaderSolution
from adventofcode2021.utils.graph import Graph


class Day12:
    g: Graph

    def create_graph(self, input_data: list[str]):
        self.g = Graph()
        for line in input_data:
            start, end = line.split("-")
            self.g.add_edge(start, end)


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_graph(input_data.splitlines())

        return 0


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
