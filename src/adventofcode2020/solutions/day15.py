from collections import defaultdict
from typing import DefaultDict

from adventofcode2020.utils.abstract import FileReaderSolution


class Day15:
    number_storage: DefaultDict[int, list]
    round: int

    def process_number(self, number: int) -> int:
        spoken_list = self.number_storage[number]
        if len(spoken_list) == 0:
            # Has never been spoken before, add it to the list and return 0
            self.number_storage[number] = [self.round]
            return 0
        elif len(spoken_list) == 1:
            # Has been spoken once before, add new round to the list and return
            # 0 ?
            self.number_storage[0].append(self.round)
            return 0
        else:
            # Has been spoken a few times before, fetch the latests rounds:
            diff = self.number_storage[number][-1] - self.number_storage[number][-2]
            self.number_storage[diff].append(self.round)
            return diff


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        start_numbers = [int(nr.strip()) for nr in input_data.split(",")]

        # Defaultdict will store the number + the rounds that it was last used
        self.number_storage = defaultdict(list)
        self.round = 1

        for number in start_numbers:
            self.process_number(number)
            self.round += 1
        else:
            number = 0

        while self.round <= 2020:
            number = self.process_number(number)
            self.round += 1

        return number


class Day15PartB(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
