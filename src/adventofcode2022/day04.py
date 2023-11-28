from parse import parse

from adventofcode.utils.abstract import FileReaderSolution


class Day04(FileReaderSolution):
    @staticmethod
    def in_range(range1: range, range2: range) -> bool:
        raise NotImplementedError

    def solve(self, input_data: str) -> int:
        ranges = self.parse(input_data.splitlines())
        return sum(
            self.in_range(range1, range2) or self.in_range(range2, range1)
            for range1, range2 in ranges
        )

    @staticmethod
    def parse(lines) -> list[tuple[range, range]]:
        ranges = []
        for line in lines:
            p = parse("{start1:d}-{stop1:d},{start2:d}-{stop2:d}", line)
            ranges.append(
                (range(p["start1"], p["stop1"] + 1), range(p["start2"], p["stop2"] + 1))
            )
        return ranges


class Day04PartA(Day04):
    @staticmethod
    def in_range(range1: range, range2: range) -> bool:
        return all(i in range2 for i in range1)


class Day04PartB(Day04):
    @staticmethod
    def in_range(range1: range, range2: range) -> bool:
        return any(i in range2 for i in range1)
