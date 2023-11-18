from __future__ import annotations

import tqdm

from adventofcode2016.utils.abstract import FileReaderSolution

SAFE = "."
TRAP = "^"


class Day18:
    @staticmethod
    def is_safe(above: list) -> bool:
        """Calculate is we are in a safe or dangerous spot"""
        # Then, a new tile is a trap only in one of the following situations:

        # Its left and center tiles are traps, but its right tile is not
        if above[0] == above[1] == TRAP and above[2] == SAFE:
            return False
        # Its center and right tiles are traps, but its left tile is not.
        if above[1] == above[2] == TRAP and above[0] == SAFE:
            return False
        # Only its left tile is a trap.
        if above[0] == TRAP and above[1] == above[2] == SAFE:
            return False
        # Only its right tile is a trap.
        if above[0] == above[1] == SAFE and above[2] == TRAP:
            return False
        return True

    @classmethod
    def evolve(cls, input_string: str) -> str:
        """Game of live with safe spaces :)"""
        result = []
        length = len(input_string)
        for idx in range(length):
            above = []
            for i in (-1, 0, 1):
                if i + idx < 0 or i + idx >= length:
                    above.append(SAFE)
                else:
                    above.append(input_string[i + idx])

            # above now contains the items above us, time to calculate:
            if cls.is_safe(above):
                result.append(SAFE)
            else:
                result.append(TRAP)

        return "".join(result)

    def calculate(self, line: str, rows: int) -> int:
        safe_spaces = 0
        for _ in tqdm.trange(rows):
            safe_spaces += line.count(SAFE)
            line = self.evolve(line)
        return safe_spaces


class Day18PartA(Day18, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.calculate(input_data.strip(), 40)


class Day18PartB(Day18, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.calculate(input_data.strip(), 400_000)
