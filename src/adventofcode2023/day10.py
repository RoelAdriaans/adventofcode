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
        # If the name is "SS", it is the starting position, and might now have south.
        return "S" in self.name and self.name != "SS"

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


class Day10:
    grid: dict[tuple[int, int], str]
    max_row: int
    max_col: int
    start_point = tuple[int, int]

    def parse(self, input_data: str):
        self.grid = {}
        for row_idx, row in enumerate(input_data.splitlines()):
            for col_idx, char in enumerate(row):
                self.grid[(row_idx, col_idx)] = char
                if char == "S":
                    self.start_point = (row_idx, col_idx)
                self.max_row = row_idx
                self.max_col = col_idx

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
        # Also, get the start type and update it in the grid
        valid_directions = []
        for direction in [(1, 0, "S"), (0, 1, "E"), (-1, 0, "N"), (0, -1, "W")]:
            if (
                self.start_point[0] + direction[0],
                self.start_point[1] + direction[1],
            ) in connections:
                valid_directions.append(direction[2])
        direction = "".join(valid_directions)

        try:
            replacement = Tile[direction]
        except KeyError:
            replacement = Tile[direction[::-1]]

        self.grid[self.start_point] = replacement.value

        # Let's follow the path
        cur_point = connections[0]
        path = [self.start_point, cur_point]
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
            if len(next_step) == 0:
                # We have found the loop, nowhere to go
                return path

            next_step = next_step[0]
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
    def raytracing(
        self, path: list[tuple[int, int]], row: int
    ) -> list[tuple[int, int]]:
        """Return a list if points that are inside the path"""
        outside_points = []
        outside = True
        start_f = None
        for col in range(self.max_col + 1):
            char = self.grid[(row, col)]
            if char == "." and not outside:
                # We are outside, and hit an empty spot!
                outside_points.append((row, col))

            elif char == "|":
                outside = not outside

            elif char == "F":
                start_f = True

            elif char == "L":
                start_f = False

            elif char == "-":
                # Alongside a wall, can only happen if not with bend
                if start_f is None:
                    raise ValueError("Horizontal line but outside?!")

            elif char == "7":
                # End of a pipe
                if start_f is None:
                    raise ValueError("Horizontal end `7`, but not started!?")
                if not start_f:
                    outside = not outside
                start_f = None

            elif char == "J":
                if start_f is None:
                    raise ValueError("Horizontal end `J`, but not started!?")
                if start_f:
                    outside = not outside
                start_f = None
        return outside_points

    def convert_to_box_chars(self, path=None, inside=None):
        if path is None:
            path = []
        if inside is None:
            inside = []
        thin_box_chars = {
            "F": "┌",
            "7": "┐",
            "L": "└",
            "J": "┘",
            "-": "─",
            "|": "│",
            "S": "@",
            ".": " ",
            "I": "│",
        }
        thick_box_chars = {
            "F": "╔",
            "7": "╗",
            "L": "╚",
            "J": "╝",
            "-": "═",
            "|": "║",
            "S": "@",
            ".": " ",
            "I": "║",
        }
        grid = {}
        for row_idx in range(self.max_row + 1):
            for col_idx in range(self.max_col + 1):
                loc = (row_idx, col_idx)
                if loc in inside:
                    grid[loc] = "I"
                elif loc in path:
                    grid[loc] = thick_box_chars[self.grid[loc]]
                else:
                    grid[loc] = thin_box_chars[self.grid[loc]]

        return grid

    def print_grid(self, grid):
        print()
        lines = []
        for row in range(self.max_row + 1):
            lines.append("".join([grid[(row, col)] for col in range(self.max_col + 1)]))
        print("\n".join(lines))
        print()

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        path = self.find_path()

        # First cleanup the grid. Everything that is not in path, or Start!
        # will become a "."
        for location, tile in self.grid.items():
            if tile != "." and tile != "S" and location not in path:
                self.grid[location] = "."

        valid_points = 0
        inside = []
        for row in range(0, self.max_row + 1):
            inside_points = self.raytracing(path, row)
            valid_points += len(inside_points)
            inside.extend(inside_points)

        print(self.print_grid(self.convert_to_box_chars(path, inside)))

        return valid_points
