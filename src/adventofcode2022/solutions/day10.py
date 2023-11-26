from typing import NamedTuple

from adventofcode.utils.abstract import FileReaderSolution


class Instruction(NamedTuple):
    instruction: str
    value: int | None


class ProgramEnded(Exception):  # noqa: N818
    """Signal that the program has ended"""


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
        if self.program_counter >= len(self.instructions):
            raise ProgramEnded

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
            if current_instruction.value:
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

    @staticmethod
    def fill_buffer(instructions: list[Instruction]) -> list[int]:
        cpu = CPU(instructions)
        frame_buffer = []
        while True:
            frame_buffer.append(cpu.x)
            try:
                cpu.cycle()
            except ProgramEnded:
                break
        return frame_buffer


class Day10PartA(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = self.parse(input_data=input_data)
        frame_buffer = self.fill_buffer(instructions)
        total = 0
        for cycle in (20, 60, 100, 140, 180, 220):
            total += cycle * frame_buffer[cycle - 1]

        return total


ON = "#"
OFF = "."


class Day10PartB(Day10, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        instructions = self.parse(input_data=input_data)

        frame_buffer = self.fill_buffer(instructions)

        screen = [[OFF] * 40 for _ in range(6)]

        for row in range(6):
            for col in range(40):
                counter = row * 40 + col
                if abs(frame_buffer[counter] - col) <= 1:
                    screen[row][col] = ON

        return "\n".join("".join(line) for line in screen)
