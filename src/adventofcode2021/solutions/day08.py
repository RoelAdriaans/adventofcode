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

        accepted_values = (2, 4, 3, 7)

        result = [
            len(value) in accepted_values
            for pattern in patterns
            for value in pattern[1]
        ]
        return sum(result)


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
