from __future__ import annotations

import logging
import math
from collections import defaultdict

from adventofcode.utils.abstract import FileReaderSolution

_logger = logging.getLogger(__name__)


class Day06:
    pass


class Day06PartA(Day06, FileReaderSolution):
    @staticmethod
    def do_math(sums: list) -> int:
        """Do the math, based on the input"""
        grand_total = 0
        for column in sums:
            operator = column[-1]
            numbers = list(map(int, column[:-1]))
            if operator == "+":
                grand_total += sum(numbers)
            elif operator == "*":
                grand_total += math.prod(numbers)
            else:
                raise ValueError("Operator not recognized")
        return grand_total

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        columns = [line.split() for line in lines]

        # Transpose the columns to rows
        rows = list(zip(*columns))

        return self.do_math(rows)


class Day06PartB(Day06, FileReaderSolution):
    @staticmethod
    def add_numbers(numbers: defaultdict, operator: str) -> int:
        numbers = [int("".join(map(str, x))) for x in numbers.values()]
        if operator == "+":
            return sum(numbers)
        elif operator == "*":
            return math.prod(numbers)
        else:
            raise ValueError("Operator not recognized")

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()

        # Add missing spaces
        max_length = max(len(line) for line in lines)
        lines = [line.ljust(max_length, " ") for line in lines]

        grand_total = 0

        numbers = defaultdict(list)
        operator = None
        for column in range(max_length - 1, -1, -1):
            _logger.debug("Processing column %d", column)
            # If this column is empty, add the numbers
            if not any(x.strip() for x in [line[column] for line in lines]):
                # Convert numbers into an array
                grand_total += self.add_numbers(numbers, operator)
                numbers = defaultdict(list)
                operator = None
                continue

            for row in range(len(lines)):
                char = lines[row][column]
                if char.isdigit():
                    numbers[column].append(int(char))
                elif char in "+*":
                    operator = char

        # Add the final set of numbers to the grand total
        grand_total += self.add_numbers(numbers, operator)
        return grand_total
