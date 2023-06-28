import itertools
import re

from adventofcode2016.utils.abstract import FileReaderSolution


class Day03:
    @staticmethod
    def is_valid_triangle(sides: list[int]) -> bool:
        """Return if this is a valid triangle"""
        sides = sorted(sides)
        return sides[0] + sides[1] > sides[2]

    @staticmethod
    def _split_into_parts(input_data: str) -> list[list[int, int, int]]:
        find_digits_re = re.compile(r"\s*(\d+)\s+(\d+)\s+(\d+)\s*")
        lines = input_data.splitlines()
        res = []
        for line in lines:
            m = re.match(find_digits_re, line)
            sides = [int(m.group(1)), int(m.group(2)), int(m.group(3))]
            res.append(sides)
        return res


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(
            self.is_valid_triangle(side) for side in self._split_into_parts(input_data)
        )


class Day03PartB(Day03, FileReaderSolution):
    def find_triangles(self, input_lines: str) -> list[list[int, int, int]]:
        """Parse the input and return a list of triangles"""
        list_if_sides = self._split_into_parts(input_lines)
        # Transpose
        transposed = zip(*list_if_sides)
        # And now, chain everything together to create one big list again, in groups
        # of 3.
        grouped = [iter(itertools.chain(*transposed))] * 3
        return zip(*grouped)

    def solve(self, input_data: str) -> int:
        return sum(
            self.is_valid_triangle(side) for side in self.find_triangles(input_data)
        )
