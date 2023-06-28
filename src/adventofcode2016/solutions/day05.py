from __future__ import annotations

import hashlib
import logging

from adventofcode2016.utils.abstract import FileReaderSolution


class Day05:
    pass


class Day05PartA(Day05, FileReaderSolution):
    @staticmethod
    def find_match(prefix: str, starting: int) -> tuple[str, int]:
        """With prefix, start at a specific number. Return the value of the first
        non-zero number, and the current position"""
        position = starting
        while True:
            pos_hash = hashlib.md5(f"{prefix}{position}".encode()).hexdigest()
            if pos_hash[:5] == "00000":
                return pos_hash[5], position
            position += 1

    def solve(self, input_data: str) -> str:
        prefix = input_data.strip()
        result = []
        current_location = 0
        for _ in range(8):
            found, current_location = self.find_match(prefix, current_location + 1)
            logging.debug("Found digit %s at location %d", found, current_location)
            result.append(found)

        return "".join(result)


class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
