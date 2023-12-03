from __future__ import annotations

from collections import defaultdict
from math import prod

import attrs

from adventofcode.utils.abstract import FileReaderSolution


@attrs.define(frozen=True)
class Symbol:
    symbol: str
    row: int
    col: int


class Day03:
    grid: list[list[str]]

    def parse_into_parts(self, input_data: str) -> list[tuple[int, Symbol]]:
        """Parse into a list of integers with symbols connected"""
        # Create a row/col grid from the input data
        self.grid = [list(line) for line in input_data.splitlines()]
        part_numbers = []
        for row in range(0, len(self.grid)):
            is_digit = False
            current_digits = []
            for col in range(0, len(self.grid[0])):
                if self.grid[row][col].isdigit():
                    is_digit = True
                    # If we're working on a digit, add it to the running total
                    current_digits.append(self.grid[row][col])
                else:
                    # Not a digit anymore, validate
                    if current_digits and (
                        symbol := self.validate(current_digits, row, col - 1)
                    ):
                        part_numbers.append((int("".join(current_digits)), symbol))
                    is_digit = False
                    current_digits = []
            # We have reached the edge, check if we have a valid digit in the bugger
            if is_digit and (symbol := self.validate(current_digits, row, col)):
                part_numbers.append((int("".join(current_digits)), symbol))

        return part_numbers

    @staticmethod
    def check_symbol(input_value: str) -> bool:
        if input_value.isdigit():
            return False
        if input_value == ".":
            return False
        return True

    def validate(self, digits, row, col) -> bool | Symbol:
        """Validate if the digits in are real. If they are real, return a Symbol"""
        # If we end at column 5 with 3 digits, we need to check
        # (eg, col - len(digits) ...  col+1)
        # 23456
        min_col = col - len(digits)
        max_col = col + 1
        # Check above and below the current row
        for check_row in (row - 1, row, row + 1):
            for check_col in range(min_col, max_col + 1):
                try:
                    if self.check_symbol(self.grid[check_row][check_col]):
                        return Symbol(
                            self.grid[check_row][check_col], check_row, check_col
                        )
                except IndexError:
                    # Index out of bounds, ignoring
                    pass
        return False


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        part_numbers = self.parse_into_parts(input_data)
        res = sum([number for number, _ in part_numbers])
        return res


class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        part_numbers = self.parse_into_parts(input_data)
        # Find the symbols with a *
        valid_parts = [
            (value, symbol) for value, symbol in part_numbers if symbol.symbol == "*"
        ]
        # Convert the row/col locations to see if we have duplicates
        locations: defaultdict[Symbol, list] = defaultdict(list)
        for amount, symbol in valid_parts:
            locations[symbol].append(amount)

        # Add the total if we have 2 (or more?!?) amounts on one location
        total = 0
        for value in locations.values():
            if len(value) >= 2:
                total += prod(value)
        return total
