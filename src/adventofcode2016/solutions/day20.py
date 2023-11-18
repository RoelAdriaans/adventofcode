from __future__ import annotations

import logging

from adventofcodeutils.parsing import extract_digits_from_string

from adventofcode2016.utils.abstract import FileReaderSolution


class Day20:
    @staticmethod
    def find_lowest(input_data: str) -> int:
        pairs = [extract_digits_from_string(line) for line in input_data.splitlines()]
        logging.debug("%s pairs", len(pairs))

        _, *starts = sorted([p[0] for p in pairs])
        ends = sorted([p[1] for p in pairs])
        for start_zip, end_zip in zip(starts, ends):
            if start_zip > end_zip + 1:
                return end_zip + 1
        raise ValueError("No gap found")

    @staticmethod
    def find_all(input_data: str, max_number: int) -> int:
        pairs = [extract_digits_from_string(line) for line in input_data.splitlines()]
        logging.debug("%s pairs", len(pairs))

        _, *starts = sorted([p[0] for p in pairs])
        *ends, end = sorted([p[1] for p in pairs])

        count = 0
        for start_zip, end_zip in zip(starts, ends):
            if start_zip > end_zip + 1:
                count += 1
        # And we need to find out the number of ip's at the end:
        # Lets say, end is 8, max_number is 9, that's one:
        count += max_number - end
        return count


class Day20PartA(Day20, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.find_lowest(input_data)


class Day20PartB(Day20, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.find_all(input_data, 4294967295)
