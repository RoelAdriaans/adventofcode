from __future__ import annotations

import logging

import more_itertools

from adventofcode.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


class Day12:
    def count_arrangements(self, line: str) -> int:
        """Count the arrangements that this group can make.

        - We need to change the `?` into `#` or `.`
        - After the change, the groups still must be valid -> Check with is_valid
        - Groups is in order (!!), eg 1, 2, 3 -> #.##.###, NOT ###.##.#
        """
        # For a line, calculate how many arrangements we can make
        conditions, groups = line.split()
        groups = [int(g) for g in groups.split(",")]

        # Indexes contain the indexes of all the ? characters
        indexes = [idx for idx, char in enumerate(conditions) if char == "?"]

        # Now, I want to replace them all with # or ?, and check if they are a valid
        # arrangement.
        valid_arrangements = set()
        for replacements in more_itertools.powerset(indexes):
            copy = list(conditions)
            for replacement in replacements:
                copy[replacement] = "#"
            copy = "".join(copy).replace("?", ".")

            if self.is_valid_arrangement(copy, groups):
                logger.debug("Valid arrangement %s", copy)
                valid_arrangements.add(copy)
        return len(valid_arrangements)

    @staticmethod
    def is_valid_arrangement(line: str, groups: list[int]) -> bool:
        """Test that this is a valid arrangement"""
        part_lengths = [len(p) for p in line.split(".") if len(p) > 0]
        return part_lengths == groups


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(self.count_arrangements(line) for line in input_data.splitlines())


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
