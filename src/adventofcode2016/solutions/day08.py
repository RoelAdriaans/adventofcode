from __future__ import annotations

import re
from enum import Enum, auto

import attrs

from adventofcode2016.utils.abstract import FileReaderSolution
from adventofcode2016.utils.advent_utils import extract_digits_from_string


class Operation(Enum):
    rect = auto()
    rotate = auto()


class Direction(Enum):
    row = auto()
    column = auto()


@attrs.define
class Instruction:
    operation: Operation
    direction: Direction | None
    x: int
    y: int
    dy: int
    dx: int

    @classmethod
    def from_string(cls, instruction_string: str) -> Instruction:
        """Parse into"""
        x, y, dx, dy = 0, 0, 0, 0
        locations = extract_digits_from_string(instruction_string)
        operation = None
        direction = None
        # This would have been a nice case for match statement..
        if instruction_string.startswith("rect"):
            operation = Operation.rect
            x = locations[0]
            y = locations[1]

        elif instruction_string.startswith("rotate row"):
            operation = Operation.rotate
            direction = Direction.row
            y = locations[0]
            dy = locations[1]
        elif instruction_string.startswith("rotate column"):
            operation = Operation.rotate
            direction = Direction.column
            x = locations[0]
            dx = locations[1]

        return Instruction(
            operation=operation, direction=direction, x=x, y=y, dx=dx, dy=dy
        )


class Day08:
    pass


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
