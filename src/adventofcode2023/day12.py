from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class Day12:
    def count_arrangements(self, line: str) -> int:
        # For a line, calculate how many arrangements we can make
        conditions, groups = line.split()
        groups = [int(g) for g in groups.split(",")]
        return -1


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(self.count_arrangements(line) for line in input_data.splitlines())


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
