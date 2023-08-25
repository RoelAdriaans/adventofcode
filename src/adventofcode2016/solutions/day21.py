from __future__ import annotations

from collections import deque

import regex_spm

from adventofcode2016.utils.abstract import FileReaderSolution


class Day21:
    @staticmethod
    def run_instructions(instructions: list[str], starting: str) -> str:
        password = deque(starting.strip())
        for instruction in instructions:
            match regex_spm.fullmatch_in(instruction):
                case r"swap position (?P<x>\d) with position (?P<y>\d)" as m:
                    x, y = int(m["x"]), int(m["y"])
                    password[x], password[y] = password[y], password[x]

                case r"swap letter (?P<x>\D) with letter (?P<y>\D)" as m:
                    x = password.index(m["x"])
                    y = password.index(m["y"])
                    password[x], password[y] = password[y], password[x]

                case r"rotate left (?P<x>\d) steps?" as m:
                    password.rotate(int(m["x"]) * -1)
                case r"rotate right (?P<x>\d) steps?" as m:
                    password.rotate(int(m["x"]))
                case r"rotate based on position of letter (?P<x>\D)" as m:
                    index = password.index(m["x"]) + 1
                    if index > 4:
                        index += 1
                    password.rotate(index)

                case r"reverse positions (?P<x>\d) through (?P<y>\d)" as m:
                    # Stupid slow, but it might just work:
                    x, y = int(m["x"]), int(m["y"]) + 1
                    password_list = list(password)
                    start, rot, end = (
                        password_list[:x],
                        list(reversed(password_list[x:y])),
                        password_list[y:],
                    )
                    password = deque([*start, *rot, *end])

                case r"move position (?P<x>\d) to position (?P<y>\d)" as m:
                    x, y = int(m["x"]), int(m["y"])
                    # First rotate the position into place
                    password.rotate(x * -1)
                    remove = password.popleft()

                    # Next, slide to the place where we want it
                    password.rotate(x + y * -1)
                    password.appendleft(remove)
                    # And rotate back
                    password.rotate(y)

                case _:
                    raise ValueError("Unknown Instruction: %s", instruction)
        return "".join(password)


class Day21PartA(Day21, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        instructions = input_data.splitlines()
        return self.run_instructions(instructions, "abcdefgh")


class Day21PartB(Day21, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
