from __future__ import annotations

from collections import deque
from collections.abc import Callable
from functools import cache

import attrs
from adventofcodeutils.generic_search import Astar

from adventofcode2016.utils.abstract import FileReaderSolution


@attrs.define(frozen=True)
class MazeLocation:
    x: int
    y: int
    steps: int = attrs.field(eq=False, default=0)


class Maze:
    favourite_number: int
    start: MazeLocation
    goal: MazeLocation
    max_steps: int

    def __init__(
        self,
        favourite_number: 10,
        start: MazeLocation = MazeLocation(1, 1),
        goal: MazeLocation = MazeLocation(31, 39),
        max_steps: int = 0,
    ):
        self.favourite_number = favourite_number
        self.start = start
        self.goal = goal
        self.max_steps = max_steps

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> list[MazeLocation]:
        locations: list[MazeLocation] = []

        # We cannot move diagonally,
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        for x, y in directions:
            location = MazeLocation(x=ml.x + x, y=ml.y + y, steps=ml.steps + 1)

            if self.max_steps > 0 and location.steps > self.max_steps:
                continue

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
    def bfs(self, maze: Maze) -> int:
        """Run BFS on the maze, and return the length of seen"""
        frontier: deque[MazeLocation] = deque()
        frontier.append(maze.start)

        # Explored is where we have been
        explored: set[MazeLocation] = {maze.start}

        # keep going while there is more to explore
        while frontier:
            current_location = frontier.popleft()
            for child in maze.successors(current_location):
                if child in explored:
                    # skip children we already explored
                    continue
                explored.add(child)
                frontier.append(child)

        # No more children to add, frontier is empty.
        # We have found every location that's maze.max_steps steps away
        return len(explored)

    def solve(self, input_data: str) -> int:
        # Creating a new maze. Goal will be at a high location, we will bail out
        # earlier if we cannot move further
        m = Maze(
            favourite_number=int(input_data.strip()),
            start=MazeLocation(1, 1),
            goal=MazeLocation(99, 99),
            max_steps=50,
        )

        # Implement BFS, so that we can keep the results
        return self.bfs(maze=m)
