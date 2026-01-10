from __future__ import annotations

from functools import cache

from adventofcode.utils.abstract import FileReaderSolution


class Day07:
    start: tuple[int, int]
    splitters: set[tuple[int, int]]
    height: int

    def parse_grid(self, input_data: str):
        lines = input_data.splitlines()
        self.height = len(lines)
        self.splitters = set()

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "S":
                    self.start = (row, col)
                elif char == "^":
                    self.splitters.add((row, col))


class Day07PartA(Day07, FileReaderSolution):
    def compute_lab(self) -> int:
        """Compute part 1"""
        # Start the BEAM!
        beams: set[tuple[int, int]] = {self.start}
        splits = 0
        for _ in range(self.height):
            new_beams = set()
            for beam in beams:
                # Get the location below the beam. If it's a splitter,
                # we add two new beams
                below = (beam[0] + 1, beam[1])
                # No splitter - just continue downwards
                if below not in self.splitters:
                    new_beams.add(below)

                elif below in self.splitters:
                    beam_left = (below[0], below[1] - 1)
                    beam_right = (below[0], below[1] + 1)
                    new_beams.add(beam_left)
                    new_beams.add(beam_right)
                    splits += 1

            beams = new_beams
        return splits

    def solve(self, input_data: str) -> int:
        self.parse_grid(input_data)
        return self.compute_lab()


class Day07PartB(Day07, FileReaderSolution):
    @cache
    def compute_timelines(self, position: tuple[int, int] = None) -> int:
        if position is None:
            # First encounter, first position is start position
            position = self.start
        if position[0] >= self.height:
            # Are we at the end?
            return 1
        # Are we on a splitter?
        if position in self.splitters:
            # Resolve left and right
            return self.compute_timelines(
                (position[0] + 1, position[1] - 1)
            ) + self.compute_timelines((position[0] + 1, position[1] + 1))
        else:
            # Continue downwards
            return self.compute_timelines((position[0] + 1, position[1]))

    def solve(self, input_data: str) -> int:
        self.parse_grid(input_data)
        return self.compute_timelines()
