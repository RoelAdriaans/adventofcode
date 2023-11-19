import re
from collections import defaultdict

from adventofcodeutils.queue import Queue

from adventofcode2021.utils.abstract import FileReaderSolution


class Day13:
    grid: defaultdict[tuple[int, int], bool]
    folds: Queue[tuple[str, int]]
    size: int

    def create_grid(self, lines: list[str]):
        self.grid = defaultdict(bool)
        for line in lines:
            j, i = line.split(",")
            self.grid[int(i), int(j)] = True
        self._set_size()

    def _set_size(self):
        self.size = max(max(i, j) for i, j in list(self.grid.keys()))

    def create_folds(self, lines: list[str]):
        p = re.compile(r"^fold along (?P<direction>[x|y])=(?P<fold_line>\d*)$")
        self.folds = Queue()
        for line in lines:
            if match := p.search(line):
                mdict = match.groupdict()
                self.folds.push((mdict["direction"], int(mdict["fold_line"])))

    def repr_grid(self):  # pragma: nocover
        lines = []
        for i in range(0, self.size + 1):
            line = "".join(
                "#" if self.grid[i, j] else "." for j in range(0, self.size + 1)
            )
            lines.append(line)
        return "\n".join(lines)

    def _fold(self):
        direction, fold_line = self.folds.pop()
        if direction == "y":
            for i in range(fold_line + 1, self.size + 1):
                for j in range(0, self.size + 1):
                    if self.grid[i, j]:
                        new_i = self._mirrored_location(i, fold_line)
                        self.grid[new_i, j] = True
        elif direction == "x":
            for j in range(fold_line + 1, self.size + 1):
                for i in range(0, self.size + 1):
                    if self.grid[i, j]:
                        new_j = self._mirrored_location(j, fold_line)
                        self.grid[i, new_j] = True

        # And then, delete everything under or left to the fold line
        for i, j in list(self.grid.keys()):
            if direction == "y":
                if i > fold_line:
                    del self.grid[i, j]
            else:
                if j > fold_line:
                    del self.grid[i, j]
        # Update the size, since we deleted stuff
        self._set_size()

    @staticmethod
    def _mirrored_location(i: int, fold: int) -> int:
        """Get the location oposide to this location, based on the fold"""
        return i - ((i - fold) * 2)

    def start_folding(self, loops=None):
        """Start the folding process.

        If loops is not specified or None, loop until we run out of folds
        """
        if not loops:
            loops = len(self.folds)

        for n in range(loops):
            self._fold()
        return True

    def count_dots(self) -> int:
        all_true = [i for i in self.grid.values() if i is True]
        return sum(all_true)


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        locations, folds = input_data.split("\n\n")

        self.create_grid(locations.splitlines())
        self.create_folds(folds.splitlines())
        self.start_folding(loops=1)
        return self.count_dots()


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        locations, folds = input_data.split("\n\n")

        self.create_grid(locations.splitlines())
        self.create_folds(folds.splitlines())
        self.start_folding()
        return self.repr_grid()
