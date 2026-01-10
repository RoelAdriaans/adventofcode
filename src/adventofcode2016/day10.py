import bisect
import logging
from collections import defaultdict

import attrs
from adventofcodeutils.parsing import extract_digits_from_string

from adventofcode.utils.abstract import FileReaderSolution


@attrs.define
class Bot:
    number: int
    # Number of chips stored in bot.
    # When the number is 2, trigger to downstream is started
    chips: list[int]
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
            chips=[],
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
        for bot, chips in values.items():
            self.bots[bot].chips = sorted(chips)

    def cascade(self, bot):
        """Do some work, and pass the chips down if needed. If output is send to an
        output_bin, return a dict with the output number as key, and chip value as value
        """
        if len(bot.chips) < 2:
            # Bot only less than 2 chips, nothing to do
            return {}
        logging.debug(
            "[Bot %s] Cascading down to %s %s and %s %s",
            bot.number,
            bot.type_high,
            bot.high_output,
            bot.type_low,
            bot.low_output,
        )

        # Two chips! Distribute them
        output_bins = {}
        if bot.type_high == "bot":
            bisect.insort(self.bots[bot.high_output].chips, bot.chips.pop())
        else:
            output_bins[bot.high_output] = bot.chips.pop()

        if bot.type_low == "bot":
            bisect.insort(self.bots[bot.low_output].chips, bot.chips.pop())
        else:
            output_bins[bot.low_output] = bot.chips.pop()
        return output_bins


class Day10PartA(Day10, FileReaderSolution):
    def run(self, a: int, b: int) -> int:
        # Run until a solution is found
        output_bin = defaultdict(list)
        while True:
            # Loop over the robots
            for n, bot in self.bots.items():
                if a in bot.chips and b in bot.chips:
                    return bot.number

                output_data = self.cascade(bot)
                for bin_nr, value in output_data:
                    output_bin[bin_nr].append(value)

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.run(61, 17)


class Day10PartB(Day10, FileReaderSolution):
    def run(self) -> int:
        # Run until a solution is found
        output_bin = defaultdict(list)
        while True:
            # Loop over the robots
            for n, bot in self.bots.items():
                output_data = self.cascade(bot)

                for bin_nr, value in output_data.items():
                    output_bin[bin_nr].append(value)
            logging.debug("Output bin: %s", dict(output_bin))

            if {1, 2, 3}.issubset(set(output_bin.keys())):
                return output_bin[0][0] * output_bin[1][0] * output_bin[2][0]

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.run()
