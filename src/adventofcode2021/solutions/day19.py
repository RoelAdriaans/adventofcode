import collections
import itertools
from typing import NamedTuple

from adventofcode2021.utils.abstract import FileReaderSolution
from adventofcode2021.utils.point import XYZPoint as Point


class Scanner(NamedTuple):
    sequence: int
    beacons: list[Point]


class AxisInfo(NamedTuple):
    axis: int
    sign: int
    diff: int


class Day19:
    scanner_positions: dict[int, Point]

    @staticmethod
    def parse_input(input_data) -> list[Scanner]:
        block = input_data.split("\n\n")
        scanners: list[Scanner] = []

        for line in block:
            lines = line.splitlines()
            # Split on spaces, scanner # will be on the 3rd split
            sequence = int(lines[0].split()[2])

            beacons = []
            for beacon_str in lines[1:]:
                beacons.append(Point(*[int(b) for b in beacon_str.split(",")]))

            scanners.append(Scanner(sequence=sequence, beacons=beacons))
        return scanners

    @staticmethod
    def x_edges_from(
        src: Scanner,
        scanners_by_id: dict[int, Scanner],
    ) -> dict[int, AxisInfo]:
        x_edges = {}
        for other in scanners_by_id.values():
            for axis in (0, 1, 2):
                for sign in (-1, 1):
                    d_x: collections.Counter[int] = collections.Counter()
                    for x, _, _ in src.beacons:
                        for other_pt in other.beacons:
                            d_x[x - other_pt[axis] * sign] += 1

                    ((x_diff, n),) = d_x.most_common(1)
                    if n >= 12:
                        x_edges[other.sequence] = AxisInfo(
                            axis=axis,
                            sign=sign,
                            diff=x_diff,
                        )
        return x_edges

    @staticmethod
    def yz_edges_from(
        src: Scanner,
        x_edges: dict[int, AxisInfo],
        scanners_by_id: dict[int, Scanner],
    ) -> tuple[dict[int, AxisInfo], dict[int, AxisInfo]]:
        y_edges = {}
        z_edges = {}

        for dst_id in x_edges:
            other = scanners_by_id[dst_id]
            for axis in (0, 1, 2):
                for sign in (-1, 1):
                    d_y: collections.Counter[int] = collections.Counter()
                    d_z: collections.Counter[int] = collections.Counter()
                    for _, y, z in src.beacons:
                        for other_pt in other.beacons:
                            d_y[y - other_pt[axis] * sign] += 1
                            d_z[z - other_pt[axis] * sign] += 1

                    ((y_diff, y_n),) = d_y.most_common(1)
                    if y_n >= 12:
                        y_edges[dst_id] = AxisInfo(
                            axis=axis,
                            sign=sign,
                            diff=y_diff,
                        )

                    ((z_diff, z_n),) = d_z.most_common(1)
                    if z_n >= 12:
                        z_edges[dst_id] = AxisInfo(
                            axis=axis,
                            sign=sign,
                            diff=z_diff,
                        )

        return y_edges, z_edges

    def compute(self, input_data: str):
        scanners: list[Scanner] = self.parse_input(input_data)
        scanners_by_id: dict[int, Scanner] = {
            scanner.sequence: scanner for scanner in scanners
        }

        self.scanner_positions = {0: Point(0, 0, 0)}
        all_points = set(scanners_by_id[0].beacons)
        todo = [scanners_by_id.pop(0)]
        while todo:
            src = todo.pop()

            x_edges = self.x_edges_from(src, scanners_by_id)
            y_edges, z_edges = self.yz_edges_from(src, x_edges, scanners_by_id)

            for k in x_edges:
                dst_x = x_edges[k].diff
                dst_y = y_edges[k].diff
                dst_z = z_edges[k].diff

                self.scanner_positions[k] = Point(dst_x, dst_y, dst_z)

                next_scanner = scanners_by_id.pop(k)
                next_scanner.beacons[:] = [
                    Point(
                        dst_x + x_edges[k].sign * pt[x_edges[k].axis],
                        dst_y + y_edges[k].sign * pt[y_edges[k].axis],
                        dst_z + z_edges[k].sign * pt[z_edges[k].axis],
                    )
                    for pt in next_scanner.beacons
                ]
                all_points.update(next_scanner.beacons)

                todo.append(next_scanner)

        return all_points


class Day19PartA(Day19, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return len(self.compute(input_data))


class Day19PartB(Day19, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.compute(input_data)

        distance = 0
        for a, b in itertools.permutations(self.scanner_positions.values(), 2):
            distance = max(distance, a.distance(b))

        return distance
