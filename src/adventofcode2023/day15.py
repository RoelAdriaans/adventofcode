from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class Day15:
    @staticmethod
    def calculate_hash(word: str) -> int:
        """Calculate a hash"""
        value = 0
        for char in word:
            ascii = ord(char)
            value += ascii
            value = value * 17
            value %= 256
        return value


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(self.calculate_hash(part) for part in input_data.strip().split(","))


class Day15PartB(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
