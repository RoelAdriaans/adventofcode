from __future__ import annotations

import functools
import itertools

from adventofcode.utils.abstract import FileReaderSolution


class Day02:
    def solve(self, input_data: str) -> int:
        ranges = input_data.split(",")
        invalid_id_accumulator = 0
        for r in ranges:
            start, end = map(int, r.split("-"))
            invalid_id_accumulator += sum(
                [
                    id_to_test
                    for id_to_test in range(start, end + 1)
                    if not self.test_valid_id(id_to_test)
                ]
            )
        return invalid_id_accumulator


class Day02PartA(Day02, FileReaderSolution):
    @staticmethod
    @functools.cache
    def test_valid_id(id_to_test: int) -> bool:
        """Test if the given ID is valid.

        A valid id is an id that does not contain any repeated digits.
        E.g. 1234 is valid, 1123 is not valid
        """
        c = str(id_to_test)
        if len(c) % 2 != 0:
            return True
        half_length = int(len(c) / 2)
        return c[:half_length] != c[half_length:]


class Day02PartB(Day02, FileReaderSolution):
    @staticmethod
    @functools.cache
    def test_valid_id(id_to_test: int) -> bool:
        """Test if the given ID is valid.

        A valid id is an id that does not contain any repeated digits.
        E.g. 1234 is valid, 1123 is not valid
        """
        c = str(id_to_test)
        for batch_size in range(1, len(c) // 2 + 1):
            if len(set(itertools.batched(c, batch_size))) == 1:
                return False
        return True
