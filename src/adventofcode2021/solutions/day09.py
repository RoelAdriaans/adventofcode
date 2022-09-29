from __future__ import annotations
from adventofcode2021.utils.abstract import FileReaderSolution


class Day09:
    @staticmethod
    def create_grid(lines) -> list[list[int]]:
        """Create an of ints from a list of strings"""
        grid = [[int(val) for val in line] for line in lines]

        return grid


class Day09PartA(Day09, FileReaderSolution):
    grid = dict[int, dict[int, int]]

    def is_spot(self, i, j) -> bool:
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

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        self.grid = self.create_grid(lines)
        low_spots = []

        # Find the low spots
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.is_spot(i, j):
                    low_spots.append(self.grid[i][j] + 1)

        return sum(low_spots)


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
