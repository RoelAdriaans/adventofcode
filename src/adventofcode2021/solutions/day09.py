from __future__ import annotations

from adventofcode2021.utils.abstract import FileReaderSolution


class Day09:
    grid: list[list[int]]

    @staticmethod
    def create_grid(lines) -> list[list[int]]:
        """Create an of ints from a list of strings"""
        grid = [[int(val) for val in line] for line in lines]

        return grid

    def get_location(self, i: int, j: int) -> int | bool:
        """Return the value of a location, or False"""
        if i < 0 or j < 0:
            # We can't index negative, with a list is will loop around
            return False
        try:
            return self.grid[i][j]
        except IndexError:
            return False

    def is_spot(self, i: int, j: int) -> bool:
        value = self.grid[i][j]
        if value == 9:
            # Will never be higher, we can exit early
            return False
        # Possible options:
        options = [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1),
        ]
        for direction in options:
            try:
                if self.grid[direction[0]][direction[1]] < value:
                    return False
            except IndexError:
                # We must be at an edge, ignore
                pass
        # Nothing false, must be alright
        return True

    def print_grid(self, highlights=None):  # pragma: no cover
        """Print the grid, and optionally put locations in highlights in bold"""
        if highlights is None:
            highlights = []
        print()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if (i, j) in highlights:
                    print(f"*{self.get_location(i, j)}* ({i}, {j})", end=";")
                else:
                    print(f"{self.get_location(i, j)} ({i}, {j})", end=";")
            print()
        return 0


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        self.grid = self.create_grid(lines)

        total_risk_level = sum(
            self.grid[i][j] + 1
            for i in range(len(self.grid))
            for j in range(len(self.grid[0]))
            if self.is_spot(i, j)
        )

        return total_risk_level


class Day09PartB(Day09, FileReaderSolution):
    def find_basins(self) -> list[set[tuple[int, int]]]:
        """Find a list of basins.

        Returns a list of basins. A basin consists of a list of (i, j) locations.
        """
        # Let's start with the low-points:
        low_points = [
            (i, j)
            for i in range(len(self.grid))
            for j in range(len(self.grid[0]))
            if self.is_spot(i, j)
        ]

        basins = []
        for point in low_points:
            locations = self.find_basin_locations(point[0], point[1])
            basins.append(locations)

        # Sort based on length:
        basins.sort(key=lambda x: len(x), reverse=True)
        return basins

    def find_basin_locations(self, i, j) -> set[tuple[int, int]]:
        """For a location (i, j), return the points in the basin"""
        if self.grid[i][j] == 9:
            # Base case
            return set()

        points = {(i, j)}
        current_value = self.grid[i][j]

        options = [
            (i + 1, j),
            (i - 1, j),
            (i, j + 1),
            (i, j - 1),
        ]
        for direction in options:
            if neighbor_value := self.get_location(direction[0], direction[1]):
                # Cells with value 9 do not count. And the next value needs to be higher
                if 8 >= neighbor_value > current_value:
                    # Valid next step, add the points
                    points.add((direction[0], direction[1]))
                    # Now to see, if we can get from here:
                    extra_points = self.find_basin_locations(direction[0], direction[1])
                    if extra_points:
                        points.update(extra_points)
        return points

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        self.grid = self.create_grid(lines)

        basins = self.find_basins()
        return len(basins[0]) * len(basins[1]) * len(basins[2])
