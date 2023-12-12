from __future__ import annotations

import abc
import hashlib
from collections.abc import Callable
from functools import cache

import attrs

from adventofcode.utils.abstract import FileReaderSolution
from adventofcode.utils.generic_search import DFS, Astar


@cache
def md5(input_string: str) -> str:
    """Calculate md5"""
    return hashlib.md5(input_string.encode(), usedforsecurity=False).hexdigest()


@attrs.define(frozen=True)
class MazeLocation:
    # Not sure yet if we need this one
    x: int
    y: int
    path: str = attrs.field(default="")

    @property
    def actual_path(self) -> str:
        return "".join(char for char in self.path if char.isupper())

    def get_openlocations(self):
        # up, down, left, and right
        directions = [(0, -1, "U"), (0, 1, "D"), (-1, 0, "L"), (1, 0, "R")]

        hash = md5(self.path)

        for idx, direction in enumerate(directions):
            # Any b, c, d, e, or f means door is open;
            # any other character (any number or a) means door is closed.
            # 0xb is 11 decimal -> to b
            if (
                int(hash[idx], 16) >= 11
                and 0 <= (self.x + direction[0]) < 4
                and 0 <= (self.y + direction[1]) < 4
            ):
                yield direction


class Maze:
    start_hash: str
    start: MazeLocation
    goal: MazeLocation

    def __init__(self, start_hash: str):
        self.start_hash = start_hash
        self.start = MazeLocation(0, 0, path=start_hash)
        self.goal = MazeLocation(3, 3)

    def goal_test(self, ml: MazeLocation) -> bool:
        # Find our goal. In the goal only x and y matter
        return ml.x == self.goal.x and ml.y == self.goal.y

    def successors(self, ml: MazeLocation) -> list[MazeLocation]:
        sucs = []
        for x, y, d in ml.get_openlocations():
            sucs.append(MazeLocation(ml.x + x, ml.y + y, ml.path + d))
        return sucs

    @staticmethod
    def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
        def distance(ml: MazeLocation) -> float:
            xdist: int = abs(ml.x - goal.x)
            ydist: int = abs(ml.y - goal.y)
            return xdist + ydist

        return distance


class Day17:
    @abc.abstractmethod
    def run_search(self, start_hash: str) -> str | int:
        raise NotImplementedError

    def solve(self, input_data: str) -> str | int:
        return self.run_search(input_data.strip())


class Day17PartA(Day17, FileReaderSolution):
    def run_search(self, start_hash: str) -> str:
        m = Maze(start_hash=start_hash)
        path = Astar.astar(
            initial=m.start,
            goal_test=m.goal_test,
            successors=m.successors,
            heuristic=Maze.manhattan_distance(m.goal),
        )
        return path.state.actual_path


class Day17PartB(Day17, FileReaderSolution):
    def run_search(self, start_hash: str) -> int:
        m = Maze(start_hash=start_hash)
        paths = DFS().search(
            initial=m.start,
            goal_test=m.goal_test,
            successors=m.successors,
            explore_all=True,
        )
        return max(len(node.state.actual_path) for node in paths)
