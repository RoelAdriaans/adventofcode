from __future__ import annotations

import math
from typing import NamedTuple

import parse

from adventofcode2022.utils.abstract import FileReaderSolution
from adventofcode2022.utils.queue import Queue


class Throw(NamedTuple):
    monkid: int
    worry_level: int


class Monkey:
    monkid: int
    items: Queue[int]
    operation: str

    test_division: int
    true_to: int
    false_to: int

    inspections: int

    def __init__(self):
        self.items = Queue()
        self.inspections = 0

    def __repr__(self):
        return (
            f"Monkey(id:{self.monkid}, inspections:{self.inspections}, "
            f"items[{repr(self.items)}])"
        )

    @staticmethod
    def from_string(data: str) -> Monkey:
        lines = [line.strip() for line in data.splitlines()]
        monkey = Monkey()

        monkey.monkid = parse.parse("Monkey {:d}:", lines[0])[0]
        for item in parse.findall("{:d}", lines[1]):
            monkey.items.push(item[0])

        monkey.operation = lines[2].split("=")[1].strip()
        monkey.test_division = parse.parse("Test: divisible by {:d}", lines[3])[0]
        monkey.true_to = parse.parse("If true: throw to monkey {:d}", lines[4])[0]
        monkey.false_to = parse.parse("If false: throw to monkey {:d}", lines[5])[0]
        return monkey

    def inspect(self) -> list[Throw]:
        """Inspect the items we have. Returns a list of Throw's"""
        throws: list[Throw] = []
        while self.items:
            self.inspections += 1
            item = self.items.pop()
            # Inspect an item
            # Appla operation
            new = self._apply_operation(item)
            # Divide by 3
            new //= 3
            if new % self.test_division == 0:
                throws.append(Throw(self.true_to, new))
            else:
                throws.append(Throw(self.false_to, new))
        return throws

    def _apply_operation(self, item):
        action = self.operation.replace("old", str(item))
        return eval(action)


class Day11:
    monkeys: list[Monkey]

    @staticmethod
    def parse(input_data: str) -> list[Monkey]:
        monkeys = [Monkey.from_string(string) for string in input_data.split("\n\n")]
        return monkeys

    def play_rounds(self, rounds: int):
        for i in range(rounds):
            self.play()

    def play(self):
        for monkey in self.monkeys:
            throws = monkey.inspect()
            # And now distribute the throws around
            for throw in throws:
                self.monkeys[throw.monkid].items.push(throw.worry_level)

    def compute_score(self):
        return math.prod(sorted(list(m.inspections for m in self.monkeys))[-2:])


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.monkeys = self.parse(input_data)
        self.play_rounds(20)
        return self.compute_score()


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
