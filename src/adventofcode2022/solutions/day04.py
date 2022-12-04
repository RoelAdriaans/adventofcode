from adventofcode2022.utils.abstract import FileReaderSolution


class Day04:
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


class Day04PartA(Day04, FileReaderSolution):
    @staticmethod
    def fully_in_range(range1: range, range2: range) -> bool:
        lst1 = list(range1)
        lst2 = list(range2)
        for i in lst1:
            if i not in lst2:
                return False
        return True

    def solve(self, input_data: str) -> int:
        ranges = self.parse(input_data.splitlines())
        total = 0
        for range1, range2 in ranges:
            if self.fully_in_range(range1, range2) or self.fully_in_range(
                range2, range1
            ):
                total += 1
        return total


class Day04PartB(Day04, FileReaderSolution):
    @staticmethod
    def any_in_range(range1: range, range2: range) -> bool:
        lst1 = list(range1)
        lst2 = list(range2)
        for i in lst1:
            if i in lst2:
                return True
        return False

    def solve(self, input_data: str) -> int:
        ranges = self.parse(input_data.splitlines())
        total = 0
        for range1, range2 in ranges:
            if self.any_in_range(range1, range2) or self.any_in_range(range2, range1):
                total += 1
        return total
