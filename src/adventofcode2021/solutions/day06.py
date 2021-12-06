import logging
from typing import Optional

from adventofcode2021.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


class Lanternfish:
    age: int

    def __init__(self, age: int):
        self.age = age

    def tick(self) -> Optional["Lanternfish"]:
        if self.age == 0:
            self.age = 6
            return Lanternfish(8)
        else:
            self.age -= 1

    def __repr__(self):
        return str(self.age)


class Day06:
    fish: list[Lanternfish]
    day: int

    def print_ocean(self):
        fish_ages = ",".join(str(fish) for fish in self.fish)
        if self.day == 0:
            res = f"Initial state: {fish_ages}"
        else:
            res = f"After {self.day:3} days: {fish_ages}"
        return res

    def tick(self):
        new_fish = []
        for fish in self.fish:
            if create_new_fish := fish.tick():
                new_fish.append(create_new_fish)

        # Add the end, add all the new fish in the ocean
        self.fish.extend(new_fish)
        self.day += 1


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.day = 0
        self.fish = [Lanternfish(int(age)) for age in input_data.split(",")]
        for days in range(80):
            self.tick()
        return len(self.fish)


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return -1
