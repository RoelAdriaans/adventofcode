from typing import NamedTuple

from adventofcode2022.utils.abstract import FileReaderSolution


class Instruction(NamedTuple):
    instruction: str
    value: int | None


class CPU:
    x: int
    instructions: list[Instruction]
    program_counter: int
    current_step: int

    def __init__(self, instructions: list[Instruction]):
        self.instructions = instructions

        self.x = 1
        self.program_counter = 0
        self.current_step = 0

    def cycle(self):
        current_instruction = self.instructions[self.program_counter]
        # Single cycle instructions
        if current_instruction.instruction == "noop":
            self.program_counter += 1
            self.current_step = 0
        elif current_instruction.instruction == "addx" and self.current_step == 0:
            self.current_step += 1
        elif current_instruction.instruction == "addx" and self.current_step == 1:
            self.program_counter += 1
            self.current_step = 0
            self.x += current_instruction.value

        else:
            raise ValueError("Invalid instruction %s", current_instruction)


class Day10:
    @staticmethod
    def parse(input_data: str) -> list[Instruction]:
        instructions = []
        for line in input_data.splitlines():
            parts = line.split()
            if len(parts) == 1:
                instructions.append(Instruction(instruction=parts[0], value=None))
            else:
                instructions.append(
                    Instruction(instruction=parts[0], value=int(parts[1]))
                )

        return instructions


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = self.parse(input_data=input_data)
        cpu = CPU(instructions)

        cycles = [20, 60, 100, 140, 180, 220]
        total_sums = []
        for i in range(1, max(cycles) + 1):
            cpu.cycle()
            if i + 1 in cycles:
                total_sums.append(cpu.x * (i + 1))
        return sum(total_sums)


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
