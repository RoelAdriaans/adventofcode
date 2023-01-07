from parse import parse

from adventofcode2022.utils.abstract import FileReaderSolution
from adventofcode2022.utils.point import XYPoint as Point


class Day15:
    sensors: list[Point]
    beacons: list[Point]
    distance: list[int]

    def parse(self, input_lines: list[str]):
        """Parse line:
        Sensor at x=2, y=0: closest beacon is at x=2, y=10
        """
        self.sensors = []
        self.beacons = []
        self.distance = []
        for line in input_lines:
            p = parse(
                "Sensor at x={sx:d}, y={sy:d}: closest beacon is at x={bx:d}, y={by:d}",
                line,
            )
            sensor = Point(p["sx"], p["sy"])
            beacon = Point(p["bx"], p["by"])
            distance = abs(sensor.distance(beacon))
            self.sensors.append(sensor)
            self.beacons.append(beacon)
            self.distance.append(distance)


class Day15PartA(Day15, FileReaderSolution):
    def find_positions(self, row) -> int:
        invalid_points = set()
        # Exclude the beacons on this lines
        beacons_on_row = set()

        for sensor, beacon, distance in zip(self.sensors, self.beacons, self.distance):
            if beacon.y == row:
                # We do not calculate the beacons.
                beacons_on_row.add(beacon)

            # Calculate the distande between the sensor and the row we are measuring
            if sensor.y > row:
                remainder = distance - (sensor.y - row)
            else:
                remainder = distance - (row - sensor.y)

            # Skip sensors too far away
            if remainder < 0:
                continue

            for i in range(remainder + 1):
                invalid_points.add(sensor.x + i)
                invalid_points.add(sensor.x - i)

        return len(invalid_points) - len(beacons_on_row)

    def execute(self, input_data, row=2000000) -> int:
        self.parse(input_data.splitlines())
        return self.find_positions(row)

    def solve(self, input_data: str) -> int:
        return self.execute(input_data, row=2000000)


class Day15PartB(Day15, FileReaderSolution):
    def find_frequency(self, factor: int) -> int:
        """Find the tuning frequency"""
        return -1

    def execute(self, input_data: str, factor: int) -> int:
        self.parse(input_data.splitlines())
        return self.find_frequency(factor)

    def solve(self, input_data: str) -> int:
        return self.execute(input_data, factor=4000000)
