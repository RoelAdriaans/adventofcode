from __future__ import annotations

import logging
from enum import Enum
from itertools import cycle

from adventofcode.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


class Tile(Enum):
    EMPTY = 0
    FALLING = 1
    ROCK = 2

    @staticmethod
    def show(tile) -> str:
        values = {
            Tile.EMPTY: ".",
            Tile.ROCK: "#",
            Tile.FALLING: "@",
        }
        return values[tile]


class Day17:
    pieces = {
        "-": [
            [0, 0, 1, 1, 1, 1, 0],
        ],
        "+": [
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
        ],
        "┘": [
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
        ],
        "|": [
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
        ],
        "▉": [
            [0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0],
        ],
    }

    block_generator: cycle[tuple[str, list[list[int]]]]
    step_generator: cycle[str]
    room: list[list[Tile]]
    width: int

    def _block_generator(self) -> cycle[tuple[str, list[list[int]]]]:
        return cycle(self.pieces.items())

    @staticmethod
    def _step_generator(instructions: str) -> cycle[str]:
        return cycle(instructions.strip())

    def create_room(self, instructions: str, width: int = 7):
        """Create a room, `width` tiles wide, that follows `instructions`."""
        # First ini
        self.block_generator = self._block_generator()
        self.step_generator = self._step_generator(instructions)
        self.room = [[Tile.EMPTY] * width for _ in range(3)]
        self.width = width

    def repr_room(self) -> str:
        """Represent a room"""
        output = []
        for row in self.room:
            line = ["|"]
            for item in row:
                line.append(Tile.show(item))
            line.append("|")
            output.append("".join(line))
        return "\n".join(output)

    def drop_block(self):
        """Drop the next block, and keep looping until it hits the bottom"""
        piece, blocks = next(self.block_generator)
        logger.debug("Next piece: %s", piece)
        # Add a new block in the top
        self.room.reverse()
        for line in blocks:
            self.room.append([Tile(i) for i in line])

        self.room.reverse()
        print(self.repr_room())
        print()

        while True:
            step = next(self.step_generator)
            logger.debug("Step: %s", step)
            if step == "<":
                idx = -1
            else:
                idx = 1

            # First, check if any of the pieces is against a wall
            hit_wall = False
            for line in self.room:
                if (
                    not hit_wall
                    and line[0] == Tile.FALLING
                    or line[self.width] == Tile.FALLING
                ):
                    hit_wall = True
                    logger.debug("Piece hit a wall, setting hit_wall to true")
                    continue

            # Next, can we move left or right?
            if not hit_wall:
                for line in self.room:
                    if Tile.FALLING in line:
                        line = self.move_line(line)

            print(self.repr_room())
            print()
            return

    def add_headroom(self):
        """After a block is dropped, validate that we have enough room in the top for the
        next block"""
        ...

    def calculate_height(self):
        """Calculate the heigth of the tower"""
        return -1

    @staticmethod
    def move_line(idx, line):
        """Move a line left or right"""
        return [x for x in line]


class Day17PartA(Day17, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_room(instructions=input_data, width=7)
        print(self.repr_room())
        print()

        for i in range(1):
            logger.debug("Loop %s", i)
            self.drop_block()
            self.add_headroom()

        return self.calculate_height()


class Day17PartB(Day17, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
