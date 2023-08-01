from __future__ import annotations

from collections import defaultdict

import attrs
from adventofcodeutils.graph import Graph
from adventofcodeutils.node import Node
from adventofcodeutils.parsing import extract_digits_from_string

from adventofcode2016.utils.abstract import FileReaderSolution


@attrs.define
class Bot:
    number: int
    # value n goes to bot x
    values: list[int] = attrs.field(init=False)
    low_output: int
    type_low: str

    high_output: int
    type_high: str

    @classmethod
    def from_string(cls, s: str) -> Bot:
        """Create a new bot from a string"""
        bot, n_low, n_high = extract_digits_from_string(s)
        splits = s.split()
        type_low, type_high = splits[5], splits[10]
        valid_types = ("bot", "output")
        if type_high not in valid_types or type_low not in valid_types:
            raise ValueError("Invalid outputtype in %s", s)

        return Bot(
            number=bot,
            low_output=n_low,
            type_low=type_low,
            high_output=n_high,
            type_high=type_high,
        )


class Day10:
    bots: dict[int, Bot]

    def parse(self, input_data: str):
        """Parse the instructions"""
        self.bots = {}
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
