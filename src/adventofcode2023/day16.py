from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution
from adventofcodeutils.point import XYPoint
from enum import StrEnum
from typing import NamedTuple


class Arrow(StrEnum):
    SPLIT_HORIZONTAL = "-"
    SPLIT_VERTICAL = "|"
    MIRROR_UP = "\\"
    MIRROR_DOWN = "/"
    EMPTY = "."


class Direction(StrEnum):
    LEFT = "L"
    RIGHT = "R"
    DOWN = "D"
    UP = "U"


class Beam(NamedTuple):
    location: XYPoint
    direction: Direction

    def __hash__(self):
        # return hash(self.location)
        if self.direction in (Direction.LEFT, Direction.RIGHT):
            return hash((self.location, "HORIZONTAL"))
        return hash((self.location, "VERTICAL"))

    def __eq__(self, other):
        if not isinstance(other, Beam):
            return NotImplemented
        if self.location != other.location:
            return False
        if self.direction in (Direction.LEFT, Direction.RIGHT) and other.direction in (
            Direction.RIGHT,
            Direction.LEFT,
        ):
            return True
        if self.direction in (Direction.UP, Direction.DOWN) and other.direction in (
            Direction.UP,
            Direction.DOWN,
        ):
            return True
        return False


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

    def _add_to_beams_ifnt_energized(self, beam: Beam):
        if beam not in self.energized:
            self.beams.append(beam)
        else:
            print("Not added")

    def find_energized(self) -> int:
        self.energized = set()
        self.energized.add(Beam(XYPoint(0, 0), Direction.RIGHT))

        self.beams = [Beam(XYPoint(0, 0), Direction.RIGHT)]

        while self.beams:
            beam = self.beams.pop()
            self.print_grid(self.energized, beam)

            # What is the next location?
            match beam.direction:
                case Direction.UP:
                    next_location = beam.location + XYPoint(-1, 0)
                case Direction.DOWN:
                    next_location = beam.location + XYPoint(1, 0)
                case Direction.RIGHT:
                    next_location = beam.location + XYPoint(0, 1)
                case Direction.LEFT:
                    next_location = beam.location + XYPoint(0, -1)
                case _:
                    raise ValueError("Invalid direction")

            if next_location in self.energized:
                # We have been here already, we can skip the location
                continue

            try:
                next_arrow = Arrow(self.grid[next_location])
            except KeyError:
                # Out of bounds
                continue

            # What now?
            if next_arrow == Arrow.SPLIT_HORIZONTAL and (
                beam.direction == Direction.UP or beam.direction == Direction.DOWN
            ):
                # Split into two beams
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.RIGHT))
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.LEFT))
            elif next_arrow == Arrow.SPLIT_VERTICAL and (
                beam.direction == Direction.LEFT or beam.direction == Direction.RIGHT
            ):
                # Split into two beams
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.UP))
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.DOWN))
            # Deal with \ mirror
            elif next_arrow == Arrow.MIRROR_UP and beam.direction == Direction.UP:
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.LEFT))
            elif next_arrow == Arrow.MIRROR_UP and beam.direction == Direction.DOWN:
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.RIGHT))
            elif next_arrow == Arrow.MIRROR_UP and beam.direction == Direction.RIGHT:
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.DOWN))
            elif next_arrow == Arrow.MIRROR_UP and beam.direction == Direction.LEFT:
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.UP))
            # Deal with / mirror
            elif next_arrow == Arrow.MIRROR_DOWN and beam.direction == Direction.UP:
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.RIGHT))
            elif next_arrow == Arrow.MIRROR_DOWN and beam.direction == Direction.DOWN:
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.LEFT))
            elif next_arrow == Arrow.MIRROR_DOWN and beam.direction == Direction.RIGHT:
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.UP))
            elif next_arrow == Arrow.MIRROR_DOWN and beam.direction == Direction.LEFT:
                self._add_to_beams_ifnt_energized(Beam(next_location, Direction.DOWN))

            else:
                # Beam continues on, append to the beams.
                # Could be an empty splot, or a splitter we are hitting from the wrong end
                self._add_to_beams_ifnt_energized(Beam(next_location, beam.direction))

            # Energize the current location
            self.energized.add(Beam(next_location, beam.direction))

        # We have energized everything, now to get the unique points out of the set
        return len(set(e.location for e in self.energized))

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.find_energized()


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
