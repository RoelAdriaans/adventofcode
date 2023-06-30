from __future__ import annotations

from collections import Counter

from adventofcode2016.utils.abstract import FileReaderSolution


class Day06:
    @staticmethod
    def compute_checksum(input_data: str, position: int) -> str:
        return "".join(
            Counter(line).most_common()[position][0]
            for line in zip(*input_data.splitlines())
        )


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        return self.compute_checksum(input_data, 0)


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        return self.compute_checksum(input_data, -1)
