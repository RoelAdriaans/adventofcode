from __future__ import annotations

from collections import deque

import regex_spm

from adventofcode.utils.abstract import FileReaderSolution


class Day21:
    @staticmethod
    def rotate_base_on_letter(password, letter):
        index = password.index(letter) + 1
        if index > 4:
            index += 1
        password.rotate(index)
        return password

    @staticmethod
    def run_instructions(
        instructions: list[str], starting: str, descramble: bool = False
    ) -> str:
        password = deque(starting.strip())
        for instruction in instructions:
            match regex_spm.fullmatch_in(instruction):
                case r"swap position (?P<x>\d) with position (?P<y>\d)" as m:
                    if descramble:
                        x, y = int(m["y"]), int(m["x"])
                    else:
                        x, y = int(m["x"]), int(m["y"])
                    password[x], password[y] = password[y], password[x]

                case r"swap letter (?P<x>\D) with letter (?P<y>\D)" as m:
                    if descramble:
                        x = password.index(m["y"])
                        y = password.index(m["x"])
                    else:
                        x = password.index(m["x"])
                        y = password.index(m["y"])

                    password[x], password[y] = password[y], password[x]

                case r"rotate left (?P<x>\d) steps?" as m:
                    if descramble:
                        password.rotate(int(m["x"]))
                    else:
                        password.rotate(int(m["x"]) * -1)

                case r"rotate right (?P<x>\d) steps?" as m:
                    if descramble:
                        password.rotate(int(m["x"]) * -1)
                    else:
                        password.rotate(int(m["x"]))

                case r"rotate based on position of letter (?P<x>\D)" as m:
                    if descramble:
                        # To descramble, we brute force, and check if the result of
                        # "abcde" is the same as "cdefb".rotate(x) == "abcde".
                        # We rotate to the left, since the original will rotate to the
                        # right.
                        for n in range(len(password) + 2):
                            hash = password.copy()
                            hash.rotate(n * -1)
                            to_validate = hash.copy()
                            to_validate = Day21.rotate_base_on_letter(
                                to_validate, m["x"]
                            )
                            if to_validate == password:
                                password = hash
                                break
                        else:
                            raise ValueError(
                                "No solution found for %s", "".join(password)
                            )
                    else:
                        password = Day21.rotate_base_on_letter(password, m["x"])

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
                    if descramble:
                        x, y = int(m["y"]), int(m["x"])
                    else:
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
    def solve(self, input_data: str) -> str:
        instructions = list(reversed(input_data.splitlines()))
        return self.run_instructions(instructions, "fbgdceah", descramble=True)
