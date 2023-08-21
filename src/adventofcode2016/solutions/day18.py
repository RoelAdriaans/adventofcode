from __future__ import annotations

from adventofcode2016.utils.abstract import FileReaderSolution

SAFE = "."
TRAP = "^"

class Day18:
    @staticmethod
    def evolve(input_string:str)->str:
        """Game of live with safe spaces :)"""
        input_length = len(input_string)
        result = []
        for idx, space in enumerate(input_string):
            for i in (-1, 0, 1):
                if idx+i < input_length or idx+i > input_string:
                    result.append(SAFE)
                    continue
                # Above string
                above = input_string[idx-1:idx+2]
                if above == ""


class Day18PartA(Day18, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day18PartB(Day18, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
