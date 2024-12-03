from __future__ import annotations

import re

from adventofcodeutils import parsing

from adventofcode.utils.abstract import FileReaderSolution


class Day03:
    @staticmethod
    def scan_memory(instructions: str, conditionals: bool = False) -> int:
        """Scan the memory for instructions"""
        mul_instructions = re.findall(r"mul\(\d*,\d*\)|don\'t\(\)|do\(\)", instructions)
        res = 0
        do = True
        for mul in mul_instructions:
            if conditionals and mul == "don't()":
                do = False
            elif conditionals and mul == "do()":
                do = True
            elif do and (numbers := parsing.extract_digits_from_string(mul)):
                res += numbers[0] * numbers[1]
        return res


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.scan_memory(input_data, conditionals=False)


class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.scan_memory(input_data, conditionals=True)
