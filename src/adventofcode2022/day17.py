from __future__ import annotations

import itertools
from itertools import cycle

from adventofcode.utils.abstract import FileReaderSolution


class Day17:
    pieces = {
        "-": [[1, 1, 1, 1]],
        "+": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        "┘": [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
        "|": [[1], [1], [1], [1]],
        "▉": [[1, 1], [1, 1]],
    }

    def piece_generator(self) -> cycle[tuple[str, list[list[int]]]]:
        return itertools.cycle(self.pieces.items())


class Day17PartA(Day17, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day17PartB(Day17, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
