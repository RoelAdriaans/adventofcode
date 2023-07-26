from __future__ import annotations

from enum import Enum, auto

import attrs
import numpy as np

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
    x: int
    y: int
    screen: np.ndarray

    @staticmethod
    def parse(input_data: str) -> list[Instruction]:
        return [Instruction.from_string(line) for line in input_data.splitlines()]

    def init_screen(self, x: int, y: int):
        self.x = x
        self.y = y
        self.screen = np.full((x, y), False)

    def _draw_rect(self, instruction: Instruction):
        """Draw a rectangle, (eg, put pixels on) from 0,0 until x,y in instruction"""
        for x in range(0, instruction.x):
            for y in range(0, instruction.y):
                self.screen[y, x] = True

    def _rotate(self, instruction: Instruction):
        """Rotate a row or column"""
        if instruction.direction == Direction.column:
            self.screen[:, instruction.x] = np.roll(
                self.screen[:, instruction.x], instruction.dx
            )
        else:
            self.screen[instruction.y] = np.roll(
                self.screen[instruction.y], instruction.dy
            )

    def draw_screen(self, instructions: list[Instruction]):
        for instruction in instructions:
            if instruction.operation == Operation.rect:
                self._draw_rect(instruction)
            else:
                self._rotate(instruction)


class Day08PartA(Day08, FileReaderSolution):
    def count_pixels(self) -> int:
        return int(sum(sum(self.screen)))

    def solve(self, input_data: str, x: int = 6, y: int = 50) -> int:
        instructions = self.parse(input_data)
        self.init_screen(x, y)
        self.draw_screen(instructions)
        return self.count_pixels()


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
