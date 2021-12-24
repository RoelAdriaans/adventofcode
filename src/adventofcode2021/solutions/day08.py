from typing import Tuple

from adventofcode2021.utils.abstract import FileReaderSolution


class Day08:
    @staticmethod
    def parse(input_string: str) -> Tuple[list[str], list[str]]:
        """
        Parse the input string into two components:
        - The 10 patterns we see
        - Four digit of output Value
        """
        patterns, output_value = input_string.split(" | ")
        return patterns.split(), output_value.split()


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        # Map a signal to the number of lines. Eg, number 7 uses 3 segments
        patterns = [self.parse(line) for line in input_data.splitlines() if line]

        sum = 0
        for pattern in patterns:
            # Measure how many times we have a thing with 1, 4, 7, 8:
            for value in pattern[1]:
                if len(value) in (2, 4, 3, 7):
                    sum += 1
        return sum


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
