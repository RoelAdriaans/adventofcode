from __future__ import annotations

from more_itertools import sliding_window

from adventofcode.utils.abstract import FileReaderSolution


class Day02:
    @staticmethod
    def check_valid(line: str) -> bool:
        numbers = [int(number) for number in line.split()]
        for i, j in sliding_window(numbers, 2):
            difference = abs(i - j)
            if difference == 0 or difference > 3:
                # Diff to great
                return False
        if sorted(numbers) == numbers or sorted(numbers, reverse=True) == numbers:
            return True
        return False

    def solve(self, input_data: str) -> int:
        return sum(self.check_valid(line) for line in input_data.splitlines())


class Day02PartA(Day02, FileReaderSolution):
    pass


class Day02PartB(Day02, FileReaderSolution):
    def check_valid(self, line: str) -> bool:
        for line in line.splitlines():
            # First, check if the old condition is still valid
            if super().check_valid(line):
                return True
            # We might have to remove one of the values
            line_as_numbers = list(map(int, line.split()))
            for i in range(len(line_as_numbers)):
                line_to_test = line_as_numbers[:]
                # Remove one of the numbers and see if it is valid now
                line_to_test.pop(i)
                line_str = " ".join(map(str, line_to_test))
                if super().check_valid(line_str):
                    return True
        return False
