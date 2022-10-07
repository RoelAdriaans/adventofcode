from __future__ import annotations

from collections.abc import Iterator

from adventofcode2021.utils.abstract import FileReaderSolution


class Octopus:
    def __init__(self, value: int):
        self.value = value

    def update(self) -> bool:
        """Update the value. If the value resets to 0, return true"""
        self.value = (self.value + 1) % 10
        return self.value == 0

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"


class Day11:
    grid: dict[tuple[int, int], Octopus]
    max_i: int
    max_j: int
    total_flashes: int
    total_steps: int

    def create_grid(self, lines: list[str]):
        self.grid = {}
        for i, line in enumerate(lines):
            for j, value in enumerate(line):
                self.grid[i, j] = Octopus(int(value))
        self.max_i = i
        self.max_j = j

        self.total_flashes = 0
        self.total_steps = 0

    def print_grid(self) -> str:
        """Return the grid is a single line"""
        res = []
        previous_line = 0
        for locatation, item in self.grid.items():
            if locatation[0] != previous_line:
                res.append("\n")
                previous_line = locatation[0]

            res.append(str(item))
        return "".join(res)

    def _get_neighbours(self, i, j) -> Iterator[tuple[int, int]]:
        """Get a list of neighbours for this location."""
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di == 0 and dj == 0:
                    continue
                new_i = di + i
                new_j = dj + j
                if new_i < 0 or new_i > self.max_i:
                    continue
                if new_j < 0 or new_j > self.max_j:
                    continue
                yield new_i, new_j

    def step(self) -> int:
        """Perform a step, and return the number of Octopusses that flashed"""
        # An octopus van only flash once per step.
        # If an octopus is in flashed, we cannot update it anymore, it stays 0
        flashed_octopuses = set()

        queue = list(self.grid.keys())
        for location in queue:
            octopus = self.grid[location]
            if location not in flashed_octopuses:
                flashed = octopus.update()
                if flashed:
                    flashed_octopuses.add(location)
                    # Find the neighbours for this location
                    for i, j in self._get_neighbours(*location):
                        queue.append((i, j))
        self.total_flashes += len(flashed_octopuses)
        self.total_steps += 1
        return len(flashed_octopuses)


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_grid(input_data.splitlines())
        for _ in range(100):
            self.step()
        return self.total_flashes


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_grid(input_data.splitlines())
        total_octopuses = len(self.grid)
        for i in range(1, 100000):
            flashed = self.step()
            if flashed == total_octopuses:
                return i
        return -1
