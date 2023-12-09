from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class Day09:
    @staticmethod
    def create_differences(line: str) -> list[list[int]]:
        numbers = [int(digit) for digit in line.split()]
        differences = [numbers]
        while set(numbers) != {0}:
            numbers = [
                numbers[idx + 1] - number for idx, number in enumerate(numbers[:-1])
            ]
            differences.append(numbers)
        return differences

    def calculate_line(self, line: str) -> int:
        differences = self.create_differences(line)
        # Adding numbers:
        # I need to add current last one + previous last one and add that to previous
        differences.reverse()
        previous_add = 0
        for idx, line in enumerate(differences[:-1]):
            line.append(previous_add)
            previous_add = differences[idx + 1][-1] + previous_add

        return previous_add

    def calculate_backwards_line(self, line: str) -> int:
        """Do the same as calculate_line but backwards..."""
        differences = self.create_differences(line)
        differences.reverse()
        reversed_differences = []
        for line in differences:
            reversed_differences.append(list(reversed(line)))

        previous_add = 0
        for idx, line in enumerate(reversed_differences[:-1]):
            line.append(previous_add)
            previous_add = reversed_differences[idx + 1][-1] - previous_add

        return previous_add


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum([self.calculate_line(line) for line in input_data.splitlines()])


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(
            [self.calculate_backwards_line(line) for line in input_data.splitlines()]
        )
