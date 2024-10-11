from __future__ import annotations

from enum import StrEnum
from typing import NamedTuple

from adventofcodeutils.point import XYPoint

from adventofcode.utils.abstract import FileReaderSolution


class Arrow(StrEnum):
    SPLIT_HORIZONTAL = "-"
    SPLIT_VERTICAL = "|"
    MIRROR_UP = "\\"
    MIRROR_DOWN = "/"
    EMPTY = "."

    def next_locations(self, beam: Beam):
        """Yields the directions from the location in Beam"""
        if self == Arrow.SPLIT_HORIZONTAL and (
            beam.direction == Direction.UP or beam.direction == Direction.DOWN
        ):
            # Split into two beams
            yield beam.next_beam_location(Direction.RIGHT)
            yield beam.next_beam_location(Direction.LEFT)
        elif self == Arrow.SPLIT_VERTICAL and (
            beam.direction == Direction.LEFT or beam.direction == Direction.RIGHT
        ):
            # Split into two beams
            yield beam.next_beam_location(Direction.UP)
            yield beam.next_beam_location(Direction.DOWN)
        # Deal with \ mirror
        elif self == Arrow.MIRROR_UP and beam.direction == Direction.UP:
            yield beam.next_beam_location(Direction.LEFT)
        elif self == Arrow.MIRROR_UP and beam.direction == Direction.DOWN:
            yield beam.next_beam_location(Direction.RIGHT)
        elif self == Arrow.MIRROR_UP and beam.direction == Direction.RIGHT:
            yield beam.next_beam_location(Direction.DOWN)
        elif self == Arrow.MIRROR_UP and beam.direction == Direction.LEFT:
            yield beam.next_beam_location(Direction.UP)
        # Deal with / mirror
        elif self == Arrow.MIRROR_DOWN and beam.direction == Direction.UP:
            yield beam.next_beam_location(Direction.RIGHT)
        elif self == Arrow.MIRROR_DOWN and beam.direction == Direction.DOWN:
            yield beam.next_beam_location(Direction.LEFT)
        elif self == Arrow.MIRROR_DOWN and beam.direction == Direction.RIGHT:
            yield beam.next_beam_location(Direction.UP)
        elif self == Arrow.MIRROR_DOWN and beam.direction == Direction.LEFT:
            yield beam.next_beam_location(Direction.DOWN)
        else:
            # Beam continues on, append to the beams.
            # Could be an empty splot, or a splitter we are hitting from the wrong end
            yield beam.next_beam_location(beam.direction)


class Direction(StrEnum):
    LEFT = "L"
    RIGHT = "R"
    DOWN = "D"
    UP = "U"


class Beam(NamedTuple):
    location: XYPoint
    direction: Direction

    def next_beam_location(self, direction: Direction) -> Beam:
        # What is the next location?
        match direction:
            case Direction.UP:
                return Beam(self.location + XYPoint(-1, 0), direction)
            case Direction.DOWN:
                return Beam(self.location + XYPoint(1, 0), direction)
            case Direction.RIGHT:
                return Beam(self.location + XYPoint(0, 1), direction)
            case Direction.LEFT:
                return Beam(self.location + XYPoint(0, -1), direction)
            case _:
                raise ValueError("Invalid direction")


class Day16:
    grid: dict[XYPoint, Arrow]
    max_y: int

    def parse(self, input_data: str):
        self.grid = {}
        for x, line in enumerate(input_data.splitlines()):
            for y, char in enumerate(line):
                self.grid[XYPoint(x, y)] = Arrow(char)
        self.max_y = y


class Day16PartA(Day16, FileReaderSolution):
    energized: set[Beam]
    beams: list[Beam]

    def print_grid(self, energized: set[Beam], beam: Beam):
        print()
        for x in range(self.max_y + 1):
            for y in range(self.max_y + 1):
                if XYPoint(x, y) == beam.location:
                    token = "*"
                elif (
                    Beam(XYPoint(x, y), Direction.DOWN) in energized
                    and Beam(XYPoint(x, y), Direction.LEFT) in energized
                ):
                    token = "2"
                elif Beam(XYPoint(x, y), Direction.DOWN) in energized:
                    token = "↕"
                elif Beam(XYPoint(x, y), Direction.LEFT) in energized:
                    token = "↔"
                else:
                    token = self.grid[XYPoint(x, y)]

                print(token, end="")
            print()

    def find_energized(self) -> int:
        self.energized = set()
        self.energized.add(Beam(XYPoint(0, 0), Direction.RIGHT))

        self.beams = [Beam(XYPoint(0, 0), Direction.RIGHT)]

        while self.beams:
            beam = self.beams.pop()
            # self.print_grid(self.energized, beam)
            try:
                current_arrow = Arrow(self.grid[beam.location])
            except KeyError:
                # Out of bounds
                continue
            next_locations = list(current_arrow.next_locations(beam))
            for next_location in next_locations:
                if next_location in self.energized:
                    # We have been here already, we can skip the location
                    continue

                # Energize the current location
                self.energized.add(beam)

                # Continue the beam
                self.beams.append(next_location)

        # We have energized everything, now to get the unique points out of the set
        return len({e.location for e in self.energized})

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.find_energized()


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
