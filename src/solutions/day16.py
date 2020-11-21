from typing import List

from utils.abstract import FileReaderSolution
from utils.advent_utils import string_of_single_to_list_of_ints


class Day16:
    base_pattern = [0, 1, 0, -1]

    def generate_pattern(self, num_digits: int, multiplier: int) -> List[int]:
        """
        Generate the pattern.
        `num_digits` will be the number of digits in the stream,
        `multiplier` will be the times a digit is multiplied.

        The first digit is skipped
        """
        result: List[int] = []
        while len(result) < num_digits + 1:
            for i in self.base_pattern:
                result.extend([i] * multiplier)
        # Skip the first one, and return enough digits
        res = result[1 : num_digits + 1]
        return res

    def compute_phase(self, input_signal: List[int]) -> List[int]:
        output_signal = []
        for multiplier in range(1, len(input_signal) + 1):
            matrix = self.generate_pattern(len(input_signal), multiplier)
            line_sum = sum([x * y for x, y in zip(matrix, input_signal)])
            line_sum = abs(line_sum) % 10
            output_signal.append(line_sum)
        return output_signal

    def run_phases(self, input_signal: List[int], num_phases) -> List[int]:
        for _ in range(num_phases):
            input_signal = self.compute_phase(input_signal)
        return input_signal


class Day16PartA(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        input_signal = string_of_single_to_list_of_ints(input_data)
        result = self.run_phases(input_signal, 100)

        # Convert list of ints to single integer and take only the first 8
        return int("".join([str(i) for i in result[:8]]))


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
