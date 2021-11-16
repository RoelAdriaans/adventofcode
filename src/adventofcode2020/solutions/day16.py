import re
from typing import NamedTuple

from adventofcode2020.utils.abstract import FileReaderSolution


class Ticket(NamedTuple):
    rule: str
    upper_range_1: int
    lower_range_1: int
    upper_range_2: int
    lower_range_2: int

    @staticmethod
    def parse_input(rule: str) -> "Ticket":
        """
        Parse input, for example:
        departure track: 37-608 or 623-964
        """
        regex = r"^(.*): (\d*)-(\d*) or (\d*)-(\d*)"
        results = re.match(regex, rule)

        return Ticket(
            rule=results[1],
            lower_range_1=int(results[2]),
            upper_range_1=int(results[3]),
            lower_range_2=int(results[4]),
            upper_range_2=int(results[5]),
        )

    def is_valid(self, number) -> bool:
        """Is this number valid?"""
        if (
            self.lower_range_1 <= number <= self.upper_range_1
            or self.lower_range_2 <= number <= self.upper_range_2
        ):
            return True
        else:
            return False


class Day16:
    pass


class Day16PartA(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
