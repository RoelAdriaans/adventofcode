from __future__ import annotations

from collections import deque

from adventofcode2016.utils.abstract import FileReaderSolution


class Day19:
    @staticmethod
    def presents(number_of_elves: int) -> int:
        # Add one since we're dealing with Elfs that are not zero index-based
        circle = deque(range(1, number_of_elves + 1))
        last_elf = 0
        while circle:
            circle.rotate(-1)
            last_elf = circle.popleft()
        return last_elf


class Day19PartA(Day19, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        number_of_elves = int(input_data.strip())
        return self.presents(number_of_elves)


class Day19PartB(Day19, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
