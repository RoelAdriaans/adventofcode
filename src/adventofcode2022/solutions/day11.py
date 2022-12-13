from __future__ import annotations

import parse

from adventofcode2022.utils.abstract import FileReaderSolution


class Monkey:
    monkid: int
    items: list[int]
    operation: str

    test_division: int
    true_to: int
    false_to: int

    def __init__(self):
        self.items = []

    def __repr__(self):
        return f"Monkey(id:{self.monkid}, items[{', '.join(str(i) for i in self.items)}])"

    @staticmethod
    def from_string(data: str) -> Monkey:
        lines = [line.strip() for line in data.splitlines()]
        monkey = Monkey()

        monkey.monkid = parse.parse("Monkey {:d}:", lines[0])[0]
        monkey.items = [q[0] for q in parse.findall("{:d}", lines[1])]
        monkey.operation = lines[2].split("=")[1].strip()

        return monkey


class Day11:
    monkeys: list[Monkey]

    @staticmethod
    def parse(input_data: str) -> list[Monkey]:
        monkeys = [Monkey.from_string(string) for string in input_data.split("\n\n")]
        return monkeys


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.monkeys = self.parse(input_data)

        return -1


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
