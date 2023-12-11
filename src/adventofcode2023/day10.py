from __future__ import annotations

from enum import Enum

from adventofcode.utils.abstract import FileReaderSolution


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

    @property
    def connections(self) -> list[tuple[int, int]]:
        """Return the connections from this Tile as direction tuples as (row, col)"""
        options = []
        if self.has_north:
            options.append((-1, 0))
        if self.has_east:
            options.append((0, 1))
        if self.has_south:
            options.append((1, 0))
        if self.has_west:
            options.append((0, -1))
        return options


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
    start_point = tuple[int, int]

    def parse(self, input_data: str):
        self.grid = {}
        for row_idx, row in enumerate(input_data.splitlines()):
            for col_idx, char in enumerate(row):
                self.grid[(row_idx, col_idx)] = char
                if char == "S":
                    self.start_point = (row_idx, col_idx)

    def find_path(self) -> list[tuple[int, int]]:
        # We know our startpoint, which nodes connect?
        # This is the opposite to the connections on a Tile
        connections = []
        for direction in [(1, 0, "N"), (0, 1, "W"), (-1, 0, "S"), (0, -1, "E")]:
            nb_rc = (
                self.start_point[0] + direction[0],
                self.start_point[1] + direction[1],
            )
            try:
                neighbour = self.grid[nb_rc]
                if direction[2] in Tile(neighbour).name:
                    connections.append(nb_rc)
            except KeyError:
                pass
        if len(connections) != 2:
            raise ValueError(
                f"Starting point does not have 2 connections, but : {connections}"
            )

        # Let's follow the path

        cur_point = connections[0]
        path = [cur_point]
        visited = {cur_point}

        while cur_point != self.start_point:
            tile = Tile(self.grid[cur_point])
            connections = [
                (cur_point[0] + delta[0], cur_point[1] + delta[1])
                for delta in tile.connections
            ]
            next_step = [
                connection
                for connection in connections
                if connection not in visited and connection != self.start_point
            ]
            try:
                next_step = next_step[0]
            except IndexError:
                return path

            path.append(next_step)
            visited.add(next_step)
            cur_point = next_step

        return path


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        path = self.find_path()
        steps = (len(path) + 1) // 2
        return steps


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
