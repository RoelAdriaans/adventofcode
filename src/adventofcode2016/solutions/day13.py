from __future__ import annotations

from functools import cache

from adventofcode2016.utils.abstract import FileReaderSolution


class Day13:
    @staticmethod
    @cache
    def is_pixel_wall(x: int, y: int, favourite_number: int) -> bool:
        """Is this pixel wall"""
        if x < 0 or y < 0:
            return True
        value = x * x + 3 * x + 2 * x * y + y + y * y + favourite_number
        number_of_1 = bin(value).count("1")
        # Is this number odd or even?
        return number_of_1 % 2 == 1


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
