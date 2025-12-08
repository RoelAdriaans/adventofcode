from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class Day04:
    grid: set[tuple[int, int]]

    def create_grid(self, input_data: str) -> None:
        self.grid = set()
        for r, line in enumerate(input_data.splitlines()):
            for c, char in enumerate(line):
                if char == "@":
                    self.grid.add((r, c))

    def removable_rolls(self) -> set[tuple[int, int]]:
        """Returns the set of rolls that can be removed."""

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
            (-1, -1),
            (1, 1),
            (-1, 1),
            (1, -1),
        ]
        accessible_points = set()
        for roll in self.grid:
            occupied_places = 0
            for dr, dc in directions:
                neighbor = (roll[0] + dr, roll[1] + dc)
                if neighbor in self.grid:
                    occupied_places += 1
                # We could break here for performance, but simple benchmarking
                # showed that breaking is slower than continuing the loop.
                # Moving the grid from a list to a set improved performance more.
                # if occupied_places > 4:
                #     break
            if occupied_places < 4:
                accessible_points.add(roll)
        return accessible_points


class Day04PartA(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_grid(input_data)
        return len(self.removable_rolls())


class Day04PartB(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_grid(input_data)
        total_removed = 0
        # Keep removing rolls while possible, counting how many we removed.
        while removable_rolls := self.removable_rolls():
            total_removed += len(removable_rolls)
            self.grid = self.grid - removable_rolls

        return total_removed
