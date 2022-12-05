from abc import abstractmethod
from typing import NamedTuple

from parse import parse

from adventofcode2022.utils.abstract import FileReaderSolution
from adventofcode2022.utils.stack import Stack


class Instruction(NamedTuple):
    moves: int
    source: int
    destination: int


class Day05(FileReaderSolution):
    stacks: dict[int, Stack]
    moves = list[Instruction]

    @staticmethod
    def parse_start(start_lines: str) -> dict[int, Stack]:
        lines = start_lines.splitlines()
        # Get the range:
        stack_range = int(max(lines[-1].split(" ")))
        stacks = {}
        for i in range(0, stack_range):
            # Column i
            column = 1 + (i * 4)
            items = []
            for j in range(0, len(lines) - 1):
                if lines[j][column].strip():
                    items.append(lines[j][column])
            stack: Stack[str] = Stack()
            for item in reversed(items):
                stack.push(item)
            stacks[i + 1] = stack

        return stacks

    @staticmethod
    def parse_instructions(instructions: str) -> list[Instruction]:
        instr = []
        for line in instructions.splitlines():
            res = parse("move {moves:d} from {source:d} to {destination:d}", line)
            instr.append(Instruction(res["moves"], res["source"], res["destination"]))
        return instr

    @staticmethod
    def get_tops(stacks: dict[int, Stack]) -> str:
        tops = []
        for stack in stacks.values():
            tops.append(stack.pop())
        return "".join(tops)

    @abstractmethod
    def perform_moves(self):
        raise NotImplementedError

    def solve(self, input_data: str) -> str:
        start, instructions = input_data.split("\n\n")
        self.stacks = self.parse_start(start)
        self.moves = self.parse_instructions(instructions)
        self.perform_moves()
        return self.get_tops(self.stacks)


class Day05PartA(Day05):
    def perform_moves(self):
        for move in self.moves:
            for _ in range(0, move.moves):
                self.stacks[move.destination].push(self.stacks[move.source].pop())


class Day05PartB(Day05, FileReaderSolution):
    def perform_moves(self):
        for move in self.moves:
            moved = []
            for _ in range(0, move.moves):
                moved.append(self.stacks[move.source].pop())

            for item in reversed(moved):
                self.stacks[move.destination].push(item)
