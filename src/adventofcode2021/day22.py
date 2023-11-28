from __future__ import annotations

import re
from collections import defaultdict
from itertools import filterfalse
from typing import NamedTuple

from adventofcodeutils.point import XYZPoint as Point

from adventofcode.utils.abstract import FileReaderSolution


class Step(NamedTuple):
    # Action: True is Turn On.
    action: bool

    x_start: int
    x_stop: int
    y_start: int
    y_stop: int
    z_start: int
    z_stop: int

    @staticmethod
    def from_str(input_data: str) -> Step:
        """Split on x=11..13,y=11..13,z=11..13 into a new Step object"""
        p = re.compile(
            r"(?P<action>on|off) "
            r"x=(?P<x_start>-?\d+)..(?P<x_stop>-?\d+),"
            r"y=(?P<y_start>-?\d+)..(?P<y_stop>-?\d+),"
            r"z=(?P<z_start>-?\d+)..(?P<z_stop>-?\d+)"
        )
        groups = p.search(input_data)
        if not groups:
            raise ValueError("Bad input: ", input_data)
        mdict = groups.groupdict()
        mdict["action"] = mdict["action"] == "on"
        for key, value in mdict.items():
            if key == "action":
                continue
            mdict[key] = int(value)
        return Step(**mdict)  # type: ignore


class Reboot(NamedTuple):
    on: bool
    cube: Cube

    @staticmethod
    def from_str(input_data: str) -> Reboot:
        action, points = input_data.split()
        return Reboot(action == "on", Cube.from_str(points))


class Cube(NamedTuple):
    x0: int
    x1: int
    y0: int
    y1: int
    z0: int
    z1: int

    @property
    def size(self) -> int:
        return (self.x1 - self.x0) * (self.y1 - self.y0) * (self.z1 - self.z0)

    def intersects(self, other: Cube) -> bool:
        return (
            self.x0 < other.x1
            and self.x1 - 1 >= other.x0
            and self.y0 < other.y1
            and self.y1 - 1 >= other.y0
            and self.z0 < other.z1
            and self.z1 - 1 >= other.z0
        )

    def contains(self, other: Cube) -> bool:
        return (
            self.x0 <= other.x0
            and self.x1 >= other.x1
            and self.y0 <= other.y0
            and self.y1 >= other.y1
            and self.z0 <= other.z0
            and self.z1 >= other.z1
        )

    def subtract(self, other: Cube) -> list[Cube]:
        """If `other` cube is inside this cube, split the cube into new cubes"""
        if not self.intersects(other):
            return [self]
        elif other.contains(self):
            return []

        xs = sorted((self.x0, self.x1, other.x0, other.x1))
        ys = sorted((self.y0, self.y1, other.y0, other.y1))
        zs = sorted((self.z0, self.z1, other.z0, other.z1))

        ret = []
        for x0, x1 in zip(xs, xs[1:]):
            for y0, y1 in zip(ys, ys[1:]):
                for z0, z1 in zip(zs, zs[1:]):
                    cube = Cube(x0, x1, y0, y1, z0, z1)
                    if self.contains(cube) and not cube.intersects(other):
                        ret.append(cube)
        return ret

    @staticmethod
    def from_str(input_data: str) -> Cube:
        """Split x=11..13,y=11..13,z=11..13 into a new Step object"""
        p = re.compile(
            r"x=(?P<x_start>-?\d+)..(?P<x_stop>-?\d+),"
            r"y=(?P<y_start>-?\d+)..(?P<y_stop>-?\d+),"
            r"z=(?P<z_start>-?\d+)..(?P<z_stop>-?\d+)"
        )
        groups = p.search(input_data)
        if not groups:
            raise ValueError("Bad input: ", input_data)
        mdict = groups.groupdict()
        return Cube(
            x0=int(mdict["x_start"]),
            x1=int(mdict["x_stop"]) + 1,
            y0=int(mdict["y_start"]),
            y1=int(mdict["y_stop"]) + 1,
            z0=int(mdict["z_start"]),
            z1=int(mdict["z_stop"]) + 1,
        )


class Day22:
    ...


class Day22PartA(Day22, FileReaderSolution):
    grid: defaultdict[Point, bool]

    def parse(self, input_data: str) -> list[Step]:
        return [Step.from_str(line) for line in input_data.splitlines()]

    def apply_steps(self, steps: list[Step]):
        """Apply all the steps."""
        for step in steps:
            for x in range(step.x_start, step.x_stop + 1):
                for y in range(step.y_start, step.y_stop + 1):
                    for z in range(step.z_start, step.z_stop + 1):
                        pnt = Point(x, y, z)
                        self.grid[pnt] = step.action

    def count_on(self) -> int:
        return sum(pnt for pnt in self.grid.values() if pnt)

    @staticmethod
    def apply_limit(steps: list[Step]) -> list[Step]:
        def filter_condition(step):
            return min(step[1:]) < -50 or max(step[1:]) > 50

        return list(filterfalse(filter_condition, steps))

    def solve(self, input_data: str) -> int:
        self.grid = defaultdict(bool)
        steps = self.parse(input_data)
        # Apply the limit
        steps = self.apply_limit(steps)
        self.apply_steps(steps)
        return self.count_on()


class Day22PartB(Day22, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        reboots = [Reboot.from_str(line) for line in input_data.splitlines()]

        cubes: list[Cube] = []
        for step in reboots:
            cubes = [part for cube in cubes for part in cube.subtract(step.cube)]
            if step.on:
                cubes.append(step.cube)

        return sum(cube.size for cube in cubes)
