from __future__ import annotations

import attrs

from adventofcode.utils.abstract import FileReaderSolution
from adventofcode.utils.point import XYPoint


@attrs.define(kw_only=True)
class Instruction:
    direction: str = attrs.field(validator=attrs.validators.in_(["L", "R"]))
    steps: int = attrs.field(converter=int, validator=attrs.validators.ge(0))

    @classmethod
    def from_string(cls, string: str) -> Instruction:
        direction = string[0]
        steps = int(string[1:])
        return cls(direction=direction, steps=steps)


class Day01:
    @staticmethod
    def parse_lines(input_line: str) -> list[Instruction]:
        """Parse a line, for example `R2, L3` and return as Instructions."""
        return [Instruction.from_string(x.strip()) for x in input_line.split(",")]

    @staticmethod
    def walk(instructions: list[Instruction], early_quit=False) -> XYPoint:
        """Walk the instructions that are in the list, and return an XY point.
        Starting location will be XYPoint(0, 0)
        When early_quit is enabled, we return the current location we visit twice"""
        # XY -> X = Horizontal, Y = Vertical movement
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_pos = XYPoint(0, 0)
        current_direction = 0

        visited_locations: set[tuple[int, int]] = {(0, 0)}

        for step in instructions:
            match step.direction:
                case "R":
                    # Turn 90 degrees right
                    current_direction = (current_direction + 1) % 4
                case "L":
                    # Turn 90 degrees left
                    current_direction = (current_direction - 1) % 4
                case _:
                    raise ValueError("Unknown Direction")

            # Walk the line
            if early_quit:
                for n in range(1, step.steps + 1):
                    dx = directions[current_direction][0] * n
                    dy = directions[current_direction][1] * n
                    new_step_pos = current_pos.x + dx, current_pos.y + dy

                    if new_step_pos in visited_locations:
                        return XYPoint(*new_step_pos)
                    else:
                        visited_locations.add(new_step_pos)

            dx = directions[current_direction][0] * step.steps
            dy = directions[current_direction][1] * step.steps
            current_pos.x += dx
            current_pos.y += dy

        return current_pos


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = self.parse_lines(input_line=input_data)
        new_location = self.walk(instructions)
        distance = new_location.distance(XYPoint(0, 0))
        return distance


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        instructions = self.parse_lines(input_line=input_data)
        new_location = self.walk(instructions, True)
        distance = new_location.distance(XYPoint(0, 0))
        return distance
