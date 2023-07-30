from __future__ import annotations

from collections import defaultdict

import attrs
from adventofcodeutils.graph import Graph
from adventofcodeutils.parsing import extract_digits_from_string

from adventofcode2016.utils.abstract import FileReaderSolution


class Output:
    number: int


class Bot:
    number: int
    # value n goes to bot x
    values: list[int] = attrs.field(init=False)
    low_output: int
    high_output: int

    @classmethod
    def from_string(cls, s: str) -> Bot:
        """Create a new bot from a string"""
        bot, low, high = extract_digits_from_string(s)
        return Bot(number=bot, low_output=low, high_output=high)


class Day10:
    bots: list[Bot]

    def parse(self, input_data: str):
        """Parse the instructions"""
        self.bots = []
        # Temp dict to move the 'value x goes to bot n' strings for now
        values = defaultdict(list)
        # Create the bots
        for line in input_data.splitlines():
            if line.startswith("bot"):
                new_bot = Bot.from_string(line)
                self.bots[new_bot.number] = new_bot
            else:
                value, bot = extract_digits_from_string(line)
                values[bot].append(value)

        # Process the values
        for bot, values in values.items():
            self.bots[bot].values = values

        # Create new Graph
        g = Graph()
        # Make flake8 happy, for now
        assert g

    def find_compare(self, a: int, b: int) -> int:
        return -1


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
