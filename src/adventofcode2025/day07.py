from __future__ import annotations

from collections import defaultdict

from adventofcode.utils.abstract import FileReaderSolution


class Day07:
    @staticmethod
    def compute_lab(input_data: str) -> tuple[int, int]:
        # First, let's parse the input data into a set of splitters
        splitters: set[tuple[int, int]] = set()
        lines = input_data.splitlines()
        start = None

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                if char == "S":
                    start = (row, col)
                elif char == "^":
                    splitters.add((row, col))

        # Start the BEAM!
        beams: set[tuple[int, int]] = {start}
        paths: defaultdict[tuple[int, int], int] = defaultdict(int)
        # paths[start] = 0
        splits = 0
        for _ in range(len(lines)):
            new_beams = set()
            for beam in beams:
                # Get the location below the beam. If it's a splitter,
                # we add two new beams
                below = (beam[0] + 1, beam[1])
                # No splitter - just continue downwards
                if below not in splitters:
                    new_beams.add(below)
                    # paths[below] += 1

                elif below in splitters:
                    beam_left = (below[0], below[1] - 1)
                    beam_right = (below[0], below[1] + 1)
                    new_beams.add(beam_left)
                    new_beams.add(beam_right)
                    paths[beam_left] += 1
                    paths[beam_right] += 1
                    splits += 1

            beams = new_beams

        # for row in range(len(lines)+1):
        #     for col in range(len(lines[0])):
        #         if (row, col) == start:
        #             print('S', end='')
        #         elif (row, col) in split_locations:
        #             print('X', end='')
        #         elif (row, col) in splitters:
        #             print('^', end='')
        #         elif (row, col) in beam_locations:
        #             print('|', end='')
        #         else:
        #             print('.', end='')
        #     print()
        count_paths = sum(paths.values())
        return splits, count_paths


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.compute_lab(input_data)[0]


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.compute_lab(input_data)[1]
