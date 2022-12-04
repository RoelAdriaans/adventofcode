from adventofcode2022.utils.abstract import FileReaderSolution


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
            pair1, pair2 = line.split(",")
            start1, stop1 = pair1.split("-")
            start2, stop2 = pair2.split("-")
            range1 = range(int(start1), int(stop1) + 1)
            range2 = range(int(start2), int(stop2) + 1)
            ranges.append((range1, range2))
        return ranges


class Day04PartA(Day04):
    @staticmethod
    def in_range(range1: range, range2: range) -> bool:
        return all(i in range2 for i in range1)


class Day04PartB(Day04):
    @staticmethod
    def in_range(range1: range, range2: range) -> bool:
        return any(i in range2 for i in range1)
