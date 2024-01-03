from __future__ import annotations

from enum import Enum

from adventofcode.utils.abstract import FileReaderSolution


class State(Enum):
    ROCK = "#"
    ROUND = "O"
    EMPTY = "."


class Day14:
    points: dict[tuple[int, int], State]

    def parse_inputdata(self, input_data: str):
        """Parse input data into points into"""
        self.points = {}
        for row, line in enumerate(input_data.splitlines()):
            for col, char in enumerate(line):
                if char != ".":
                    self.points[(row, col)] = State(char)

    def tumble_down_and_calculate_load(self, direction="N") -> int:
        """Tumble the rocks down and calculate the load.
        Direction can be specified, by default is North (Up)"""
        if direction != "N":
            # Maybe rotate the grid and try again? :)
            raise NotImplementedError
        total = 0
        max_row = max([p[1] for p in self.points.keys()])
        max_col = max([p[0] for p in self.points.keys()])
        for col in range(max_col + 1):
            # working on column col
            points = {k: v for k, v in self.points.items() if k[1] == col}
            # Is there a "#" in the column?
            # has_rock = any(state == State.ROCK for state in points.values())
            rock_points = tuple(k[0] for k, v in points.items() if v == State.ROCK)
            round_points = {k[0] for k, v in points.items() if v == State.ROUND}

            for point in round_points:
                new_point = point
                # Validate if we can move this point up
                while (
                    new_point - 1 not in round_points
                    and new_point - 1 not in rock_points
                    and new_point > 0
                ):
                    new_point -= 1
                if new_point != point:
                    round_points.remove(point)
                    round_points.add(new_point)
                    self.points[(new_point, col)] = State.ROUND
                    self.points[(point, col)] = State.EMPTY

            # And now we have to calculate the scores.
            row_score = 0
            for point in round_points:
                row_score += max_row - point + 1
            print(f"col {col}, score {row_score}, {max_row=}")
            total += row_score
        return total


class Day14PartA(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse_inputdata(input_data)
        return self.tumble_down_and_calculate_load()


class Day14PartB(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
