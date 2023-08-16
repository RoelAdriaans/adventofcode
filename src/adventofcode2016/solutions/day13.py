from __future__ import annotations

from collections.abc import Callable
from functools import cache

import attrs
from adventofcodeutils.generic_search import Astar

from adventofcode2016.utils.abstract import FileReaderSolution


@attrs.define(frozen=True)
class MazeLocation:
    x: int
    y: int


class Maze:
    favourite_number: int
    start: MazeLocation
    goal: MazeLocation

    def __init__(
        self,
        favourite_number: 10,
        start: MazeLocation = MazeLocation(1, 1),
        goal: MazeLocation = MazeLocation(31, 39),
    ):
        self.favourite_number = favourite_number
        self.start = start
        self.goal = goal

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> list[MazeLocation]:
        locations: list[MazeLocation] = []

        # We cannot move diagonally,
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for x, y in directions:
            location = MazeLocation(ml.x + x, ml.y + y)
            if not self.is_pixel_wall(location):
                locations.append(location)

        return locations

    @staticmethod
    def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
        def distance(ml: MazeLocation) -> float:
            xdist: int = abs(ml.x - goal.x)
            ydist: int = abs(ml.y - goal.y)
            return xdist + ydist

        return distance

    @cache
    def is_pixel_wall(self, location: MazeLocation) -> bool:
        """Is this pixel wall"""
        x, y = location.x, location.y
        if x < 0 or y < 0:
            return True
        value = x * x + 3 * x + 2 * x * y + y + y * y + self.favourite_number
        number_of_1 = bin(value).count("1")
        # Is this number odd or even?
        return number_of_1 % 2 == 1


class Day13:
    pass


class Day13PartA(Day13, FileReaderSolution):
    def run_search(
        self, favourite_number, start: MazeLocation, goal: MazeLocation
    ) -> int:
        m = Maze(favourite_number=favourite_number, start=start, goal=goal)
        path = Astar.astar(
            initial=m.start,
            goal_test=m.goal_test,
            successors=m.successors,
            heuristic=Maze.manhattan_distance(m.goal),
        )
        return len(path.node_to_path(path)) - 1

    def solve(self, input_data: str) -> int:
        res = self.run_search(
            favourite_number=int(input_data.strip()),
            start=MazeLocation(1, 1),
            goal=MazeLocation(31, 39),
        )
        return res


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
