from typing import NamedTuple

from adventofcode.utils.abstract import FileReaderSolution


class PatternMatch(NamedTuple):
    horizontal: bool
    line: int

    def value(self) -> int:
        if self.horizontal:
            return self.line * 100
        else:
            return self.line


class Day13:
    @staticmethod
    def find_match(lines: list[str], smudges: int = 0) -> int:
        """Find a horizontal match,  return the number of matches"""
        for r in range(1, len(lines)):
            above = lines[:r][::-1]
            below = lines[r:]

            if (
                sum(
                    sum(0 if a == b else 1 for a, b in zip(x, y))
                    # x, y are the rows
                    for x, y in zip(above, below)
                )
                == smudges
            ):
                return r

        return 0

    def check_pattern(self, pattern: str, smudges: int = 0) -> PatternMatch:
        lines = pattern.splitlines()
        horizontal_middle = self.find_match(lines, smudges)
        # Vertical matches
        vertical_middle = self.find_match(
            ["".join(line) for line in zip(*lines)], smudges
        )

        # Find the winner
        if horizontal_middle > vertical_middle:
            return PatternMatch(horizontal=True, line=horizontal_middle)
        else:
            return PatternMatch(horizontal=False, line=vertical_middle)


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(
            self.check_pattern(part).value() for part in input_data.split("\n\n")
        )


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(
            self.check_pattern(part, smudges=1).value()
            for part in input_data.split("\n\n")
        )
