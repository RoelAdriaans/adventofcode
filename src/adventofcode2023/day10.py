from __future__ import annotations
from enum import Enum

from adventofcode.utils.abstract import FileReaderSolution
from adventofcodeutils.point import XYPoint as Point

class Tile(Enum):
    NS = "|"  # is a vertical pipe connecting north and south.
    EW = "-"  # is a horizontal pipe connecting east and west.
    NE = "L"  # is a 90-degree bend connecting north and east.
    NW = "J"  # is a 90-degree bend connecting north and west.
    SW = "7"  # is a 90-degree bend connecting south and west.
    SE = "F"  # is a 90-degree bend connecting south and east.
    GG = "."  # is ground; there is no pipe in this tile.
    SS = "S"  # is the starting position of the animal.

    @property
    def has_north(self) -> bool:
        return "N" in self.name

    @property
    def has_east(self) -> bool:
        return "E" in self.name

    @property
    def has_south(self) -> bool:
        return "S" in self.name

    @property
    def has_west(self) -> bool:
        return "W" in self.name


class Node:
    tile: Tile
    north: Node | None
    south: Node | None
    east: Node | None
    west: Node | None

    def __init__(self, tile: Tile):
        self.tile = tile
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def __str__(self) -> str:
        return (
            f"<Node {self.tile} (^ {self.north}, > {self.east}, "
            f"V {self.south}, < {self.west})>"
        )


class Day10:
    grid: dict[tuple[int, int], str]

    def parse(self, input_data: str):
        self.grid = {}
        for row_idx, row in enumerate(input_data.splitlines()):
            for col_idx, char in enumerate(row):
                self.grid[(row_idx, col_idx)] = char
                if char == "S":
                    start_point = (col_idx, row_idx)

        # We know our startpoint, which nodes connect?



        print(start_point)

        pass


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return -1


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
