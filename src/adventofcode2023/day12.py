from __future__ import annotations

import logging

from tqdm import tqdm

from adventofcode.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)

cache = {}


class Day12:
    @staticmethod
    def count_arrangements(
        conditions: list[str],
        groups: [list[int]],
        cond_idx: int = 0,
        group_idx: int = 0,
    ) -> int:
        """Perform the arrangement in a recursive way.

        For arrangement `#??..`


        """
        try:
            return cache[str(conditions)]
        except KeyError:
            pass
        # Base cases: We are at the end of the indexing, or if there are no more ?
        # in the conditions
        if cond_idx == len(conditions) or "?" not in conditions[cond_idx:]:
            # Base case. Return 0, or ONE, since it's a valid combination?
            # Maybe we have to check if it's valid, and return that...
            if Day12.is_valid_upto(conditions, groups, cond_idx):
                return 1
            else:
                return 0

        # If the current condition is a # or ., there is nothing to do, and we continue
        # if we reach the end of the index, we bail anyway
        while conditions[cond_idx] == "#" or conditions[cond_idx] == ".":
            cond_idx += 1
            if cond_idx >= len(conditions):
                return 0

        if conditions[cond_idx] != "?":
            raise ValueError(f"Invalid condition {conditions[cond_idx]}")

        # Do recursive magic here
        total = 0
        for possible in (".", "#"):
            copy = conditions[::]
            copy[cond_idx] = possible
            if Day12.is_valid_upto(copy, groups, cond_idx):
                # We are still in a valid state, continue this path
                # total += 1
                res = Day12.count_arrangements(copy, groups, cond_idx + 1, group_idx)
                cache[str(copy)] = res
                total += res

        return total

    @staticmethod
    def is_valid_upto(conditions: list[str], groups, cond_idx):
        """Check if the current arrangement is valid upto now"""
        if "?" not in conditions:
            return Day12.is_valid_arrangement("".join(conditions), groups)
        # In which of the groups are we?
        group_idx = 0
        # How far along are we in the current group?
        group_length = 0
        # What is the current token we're currently looking at?
        current_token = False
        for n in range(cond_idx):
            if group_idx >= len(groups):
                # There are no more groups to check against.
                # if we have a # in the next conditions, there are still
                # tokens left, and the expression is not valid.
                return "#" not in conditions[n:]

            # Skip the first empty dots
            if not current_token and conditions[n] == ".":
                continue
            if conditions[n] == "?":
                # ???
                continue

            if not current_token and conditions[n] == "#":
                # Starting a new group:
                current_token = "#"
                group_length = 1
                continue

            if current_token == "#" and conditions[n] == "#":
                # We are continuing matching.
                # If the group is longer then groups[group_idx], we are in
                # an invalid state
                group_length += 1
                if group_length > groups[group_idx]:
                    return False
                # Still in a valid stop, let's continue
                continue

            if conditions[n] != current_token:
                # We are in a different token.
                # this will signal the end of a token?
                if group_length > groups[group_idx]:
                    return False
                group_idx += 1
                group_length = 0
                current_token = False

        return True

    @staticmethod
    def is_valid_arrangement(line: str, groups: list[int]) -> bool:
        """Test that this is a valid arrangement"""
        part_lengths = [len(p) for p in line.split(".") if len(p) > 0]
        return part_lengths == groups

    @staticmethod
    def unfold(line: str) -> str:
        conditions, groups = line.split()
        return f"{'?'.join([conditions] * 5)} {','.join([groups] * 5)}"

    def count(self, input_data, folded: bool = False) -> int:
        total = 0
        for line in tqdm(input_data.splitlines()):
            if folded:
                line = self.unfold(line)
            conditions, groups = line.split()
            groups = [int(g) for g in groups.split(",")]

            total += self.count_arrangements(list(conditions), groups)
        return total


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.count(input_data, folded=False)


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.count(input_data, folded=True)
