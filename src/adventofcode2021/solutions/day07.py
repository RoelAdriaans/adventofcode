import logging
from abc import ABC, abstractmethod

from adventofcode2021.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


class Day07(ABC):
    @staticmethod
    @abstractmethod
    def find_fuel_cost(positions: list[int], target: int) -> int:
        raise NotImplementedError

    def solve(self, input_data: str) -> int:
        positions = [int(x) for x in input_data.split(",")]
        # @TODO: Define a better way to find this range. We're now brute-forcing.
        #   It works, but takes ~16 seconds to find a solution
        min_pos = min(positions)
        max_pos = max(positions)
        lowest_cost = min(
            self.find_fuel_cost(positions, n) for n in range(min_pos, max_pos)
        )
        return lowest_cost


class Day07PartA(Day07, FileReaderSolution):
    @staticmethod
    def find_fuel_cost(positions: list[int], target: int) -> int:
        total_cost = 0
        for pos in positions:
            total_cost += abs(pos - target)
        return total_cost


class Day07PartB(Day07, FileReaderSolution):
    @staticmethod
    def find_fuel_cost(positions: list[int], target: int) -> int:
        total_cost = 0
        for pos in positions:
            total_cost += sum(range(1, abs(pos - target) + 1))
        return total_cost
