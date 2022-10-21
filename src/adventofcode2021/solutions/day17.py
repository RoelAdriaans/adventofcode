import logging
import re
from dataclasses import dataclass
from typing import NamedTuple

from adventofcode2021.utils.abstract import FileReaderSolution


class Point(NamedTuple):
    x: int
    y: int


@dataclass
class TargetArea:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    def __repr__(self):
        return f"target area: x={self.min_x}..{self.max_x}, {self.min_y}..{self.max_y}"

    def is_in_target(self, location: Point) -> bool:
        """Return if we are withing the target spot"""
        # This is not the best solution, but it works. Can be optimized.. :)
        if location.x in range(self.min_x, self.max_x + 1) and location.y in range(
            self.min_y, self.max_y + 1
        ):
            return True
        else:
            return False

    def overshot(self, location: Point) -> bool:
        """Returns True if the location is further away then the location"""
        if location.x > self.max_x:
            return True
        if location.y < self.min_y:
            return True
        return False


class Day17:
    def parse_str(self, line: str) -> TargetArea:
        p = re.compile(
            r"target area: x=(?P<min_x>-?\d+)..(?P<max_x>-?\d+), "
            r"y=(?P<min_y>-?\d+)..(?P<max_y>-?\d+)"
        )

        if match := p.search(line):
            mdict = match.groupdict()
            # Convert all the strings into integers
            for key, value in mdict.items():
                mdict[key] = int(value)
            return TargetArea(**mdict)  # type: ignore
        else:
            raise ValueError("Line could not be matched: ", line)

    @staticmethod
    def compute_trajectory(
        launch_speed: tuple[int, int], target: TargetArea
    ) -> int | bool:
        """Compute the trajectory and return the max height (y) from the course.
        Returns an integer with the highest path, or false if we overshot
        """
        max_y = float("-inf")
        location = Point(0, 0)
        dx, dy = launch_speed
        while not target.overshot(location):
            # Looping
            location = Point(location.x + dx, location.y + dy)
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            # Due to gravity, the probe's y velocity decreases by 1.
            dy -= 1
            max_y = max(max_y, location.y)
            if target.is_in_target(location):
                # We hit the target!
                return int(max_y)
        # We overshot, not target reachable from here
        return False


class Day17PartA(Day17, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        destination = self.parse_str(input_data)
        found_max, max_dx, max_dy = 0, 0, 0

        for dx in range(0, 23):
            for dy in range(0, 91):
                res = self.compute_trajectory((dx, dy), destination)
                if res > found_max:
                    found_max = res
                    max_dx = dx
                    max_dy = dy
        logging.info(f"{max_dx=}, {max_dy=}")
        return found_max


class Day17PartB(Day17, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        destination = self.parse_str(input_data)
        found = []

        min_dy, min_dx = float("inf"), float("inf")
        max_dy, max_dx = float("-inf"), float("-inf")

        for dx in range(1, destination.max_x + 1):
            for dy in range(destination.min_y, abs(destination.min_y)):
                res = self.compute_trajectory((dx, dy), destination)
                if res is not False:
                    min_dx = min(min_dx, dx)
                    min_dy = min(min_dy, dy)
                    max_dx = max(max_dx, dx)
                    max_dy = max(max_dy, dy)
                    found.append(res)

        logging.info(f"{min_dy=}, {max_dy=}")
        logging.info(f"{min_dx=}, {max_dx=}")

        return len(found)
