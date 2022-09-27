import logging
import re
import typing
from collections import Counter
from dataclasses import dataclass

from adventofcode2021.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


@dataclass
class Point:
    x: int
    y: int


class Day05:
    def parse_lines(self, line) -> tuple[Point, Point]:
        """ "
        Parse 2,2 -> 2,1 or 419,207 -> 419,109
        As x1,y1 -> x2,y2
        """
        regex = r"^(?P<x1>\d*),(?P<y1>\d*) -> (?P<x2>\d*),(?P<y2>\d*)$"
        matches = re.search(regex, line)
        assert matches
        p1 = Point(x=int(matches["x1"]), y=int(matches["y1"]))
        p2 = Point(x=int(matches["x2"]), y=int(matches["y2"]))
        return p1, p2

    def find_overlap(self, points: list[tuple[Point, Point]]) -> list[Point]:
        """Find the overlapping locations in the list of points"""
        locations: typing.Counter = Counter()

        for line in points:
            # Make sure that the start is lower than the end. range(5, 0) does not work

            if line[0].x == line[1].x or line[0].y == line[1].y:
                x_start = min(line[0].x, line[1].x)
                x_stop = max(line[0].x, line[1].x)
                y_start = min(line[0].y, line[1].y)
                y_stop = max(line[0].y, line[1].y)

                # Horizontal or vertical line
                for x in range(x_start, x_stop + 1):
                    for y in range(y_start, y_stop + 1):
                        locations[(x, y)] += 1
            else:
                # Vertical line. Find out the length of the vector:
                # Always 45 degree lines
                x1 = line[0].x
                x2 = line[1].x
                y1 = line[0].y
                y2 = line[1].y

                if x1 < x2:
                    length = x2 - x1
                    x_direction = 1
                else:
                    length = x1 - x2
                    x_direction = -1
                if y1 < y2:
                    y_direction = 1
                else:
                    y_direction = -1

                for i in range(length + 1):
                    debug_txt = (
                        f"For line ({line[0].x}, {line[0].y}) -> "
                        f"({line[1].x}, {line[1].y}) adding point: "
                        f"({(x1 + (i * x_direction))}, {(y1 + (i * y_direction))}) : "
                        f"{i} of {length}"
                    )
                    logger.debug(debug_txt)

                    locations[(x1 + (i * x_direction)), (y1 + (i * y_direction))] += 1

        # Filter out locations with at least 2 hits
        return [location[0] for location in locations.items() if location[1] > 1]


class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        points = []
        for line in input_data.splitlines():
            p1, p2 = self.parse_lines(line)
            if p1.x == p2.x or p1.y == p2.y:
                points.append((p1, p2))

        res = self.find_overlap(points)
        return len(res)


class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        points = []
        for line in input_data.splitlines():
            p1, p2 = self.parse_lines(line)
            points.append((p1, p2))

        res = self.find_overlap(points)
        return len(res)
