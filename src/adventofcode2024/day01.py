from __future__ import annotations

from collections import Counter

from adventofcode.utils.abstract import FileReaderSolution


class Day01:
    def parse_numbers(self, input_data) -> tuple[list[int], list[int]]:
        lines = input_data.splitlines()
        left_numbers = []
        right_numbers = []
        for line in lines:
            left, right = line.split()
            left_numbers.append(int(left))
            right_numbers.append(int(right))
        # Next sort the lists
        left_numbers.sort()
        right_numbers.sort()
        return left_numbers, right_numbers


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        left_numbers, right_numbers = self.parse_numbers(input_data)
        return sum(
            [abs(left - right) for left, right in zip(left_numbers, right_numbers)]
        )


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        left_numbers, right_numbers = self.parse_numbers(input_data)
        cnt = Counter(right_numbers)
        return sum([left * cnt[left] for left in left_numbers])
