from adventofcode2021.utils.abstract import FileReaderSolution


class Day12:
    def create_graph(self, input_data: list[str]):
        g = nx.Graph()
        for line in input_data:
            start, end = line.split("-")
            # g.add_edges_from([(start, end)])
            g.add_edge(start, end)
        return g


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        graph = self.create_graph(input_data.splitlines())

        return 0


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
