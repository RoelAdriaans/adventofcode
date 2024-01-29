import logging

from adventofcode.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


class Day07: ...


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        positions = sorted([int(x) for x in input_data.split(",")])
        # We need to converge on the middle position, so, that's our target
        target = positions[len(positions) // 2]
        lowest_cost = self.find_fuel_cost(positions, target)
        return lowest_cost

    @staticmethod
    def find_fuel_cost(positions: list[int], target: int) -> int:
        total_cost = 0
        for pos in positions:
            total_cost += abs(pos - target)
        return total_cost


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        positions = [int(x) for x in input_data.split(",")]
        min_pos = min(positions)
        max_pos = max(positions)
        lowest_cost = min(
            self.find_fuel_cost(positions, n) for n in range(min_pos, max_pos)
        )
        return lowest_cost

    @staticmethod
    def find_fuel_cost(positions: list[int], target: int) -> int:
        total_cost = 0.0
        for pos in positions:
            delta = abs(pos - target)
            total_cost += delta * (delta + 1) / 2
        return int(total_cost)
