import re

from adventofcode2016.utils.abstract import FileReaderSolution


class Day03:
    pass


class Day03PartA(Day03, FileReaderSolution):
    @staticmethod
    def is_valid_triangle(sides: list[int]) -> bool:
        """Return if this is a valid triangle"""
        sides = sorted(sides)
        return sides[0] + sides[1] > sides[2]

    def solve(self, input_data: str) -> int:
        find_digits_re = re.compile(r"\s*(\d+)\s+(\d+)\s+(\d+)\s*")
        lines = input_data.splitlines()
        count_valid = 0
        for line in lines:
            m = re.match(find_digits_re, line)
            sides = [int(m.group(1)), int(m.group(2)), int(m.group(3))]
            if self.is_valid_triangle(sides):
                count_valid += 1
        return count_valid


class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
