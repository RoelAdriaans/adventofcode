"""Solution to the Infi advent of code puzzle."""

from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class XM4S:
    """Class representing a XM-4S computer."""

    program_counter: int
    stack: list[int]
    registers: dict[str, int]
    return_value: None | int

    def __init__(self, instructions: list, x: int, y: int, z: int) -> None:
        """Initalize the XM4S instance."""
        self.program_counter = 0
        self.stack = []
        self.registers = {
            "X": x,
            "Y": y,
            "Z": z,
        }
        self.return_value = None
        self.instructions = instructions

    def compute(self) -> None:
        """Loop until res is reached and put the right value in the return_value"""
        while True:
            instruction = self.instructions[self.program_counter]
            match instruction.split():

                case ["push", register] if register in ("X", "Y", "Z"):
                    self.stack.append(self.registers[register])
                    self.program_counter += 1
                case ["push", number]:
                    self.stack.append(int(number))
                    self.program_counter += 1

                case ["add"]:
                    a = self.stack.pop()
                    b = self.stack.pop()
                    self.stack.append(a + b)
                    self.program_counter += 1

                case ["jmpos", offset]:
                    value = self.stack.pop()
                    if value >= 0:
                        self.program_counter += int(offset)
                    self.program_counter += 1

                case ["ret"]:
                    self.return_value = self.stack.pop()
                    return

                case _:
                    raise ValueError("Invalid instruction", instruction)


class Infi:
    pass


class InfiPart1(Infi, FileReaderSolution):

    def solve_for_location(self, input_data: list, x: int, y: int, z: int) -> int:
        xm4s = XM4S(input_data, x, y, z)
        xm4s.compute()
        return xm4s.return_value

    def solve(self, input_data: str) -> int:
        instructions = input_data.splitlines()
        max_cord = 30
        total = 0
        for x in range(max_cord):
            for y in range(max_cord):
                for z in range(max_cord):
                    total += self.solve_for_location(instructions, x, y, z)
        return total


class InfiPart2(Infi, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
