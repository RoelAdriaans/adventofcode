from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution
from typing import NamedTuple
from collections import Counter


class PatternMatch(NamedTuple):
    horizontal: bool
    line: int


class Day13:
    def check_pattern(self, pattern: str) -> PatternMatch:
        lines = pattern.splitlines()

        # Check for a horizontal match
        horizontal_matches = 0
        horizontal_middle = False
        # We go over line by line, if the next line matches this line, we go outwards
        # to find the number of matched lines
        for i in range(len(lines)):
            if i > len(lines):
                break
            if lines[i] != lines[i+1]:
                continue
            # WE HAVE A MATCH!
            horizontal_middle = i
            # Number of lines we have to match
            # We have lines
            # 1 2 3 4_5 6 7, where the middle is between 4 and 5
            # now we need matches (4,5), (3, 6),
            for j in range(len(lines)):
                top = horizontal_middle - j
                bottom = horizontal_middle + j
                if lines[top] == lines[bottom]:
                    horizontal_matches += 1
                else:
                    break
        print(f"horizontal: {horizontal_matches=}, {horizontal_middle=}")



        # Vertical matches
        vertical_matches = Counter(["".join(line) for line in zip(*lines)])

        # Find the winner



        return PatternMatch(False, 100)


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
