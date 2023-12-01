from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class Day01:
    pass


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        total = 0
        for line in input_data.splitlines():
            digits = [i for i in line if i.isdigit()]
            total += int("".join([digits[0], digits[-1]]))
        return total


class Day01PartB(Day01, FileReaderSolution):
    # Replace, but keep the first and last letter in place. This could be part of
    # the next word. Something that was *not* specified in the text..
    digitmap = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    def solve(self, input_data: str) -> int:
        total = 0
        for line in input_data.splitlines():
            for digit, replacement in self.digitmap.items():
                line = line.replace(digit, replacement)
            digits = [i for i in line if i.isdigit()]
            total += int("".join([digits[0], digits[-1]]))
        return total
