from collections import Counter

from utils.abstract import FileReaderSolution


class Day1PartA(FileReaderSolution):
    def solve(self, input_data: str) -> int:
        parts = input_data.split()
        total = 0
        for part in parts:
            total += eval(part)
        return total


class Day1PartB(FileReaderSolution):
    def solve(self, input_data: str) -> int:
        frequency_to_reach = 2

        visited_frequencies: Counter = Counter()
        # We start at 0, add one for frequency 0
        visited_frequencies[0] += 1
        parts = input_data.split()
        total = 0
        while True:
            for part in parts:
                total += eval(part)
                visited_frequencies[total] += 1
                if visited_frequencies[total] == frequency_to_reach:
                    return total
