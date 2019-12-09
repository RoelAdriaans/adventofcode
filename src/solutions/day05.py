from utils.abstract import FileReaderSolution
from typing import List
from solutions.intcode import IntCode


class ProgramFinished(Exception):
    pass


class Day05:
    pass


class Day05PartA(Day05, FileReaderSolution, IntCode):
    def solve(self, input_data: str) -> int:
        # Technically not 100% correct, when res is non zero, if should check that the
        # next instructions terminates the program
        instructions = list(map(int, input_data.split(",")))
        self.load_instructions(instructions)
        res = False
        try:
            while True:
                res = self.process_instruction(1)
                if res not in (0, None):
                    return res
        except ProgramFinished:
            pass
        return res


class Day05PartB(Day05, FileReaderSolution, IntCode):
    def solve(self, input_data: str) -> int:
        instructions = list(map(int, input_data.split(",")))
        self.load_instructions(instructions)
        res = self.run(5)
        return res
