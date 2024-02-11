from __future__ import annotations

import enum
import re
from functools import cached_property

import attrs

from adventofcode.utils.abstract import FileReaderSolution


class Operation(enum.Enum):
    DASH = "-"
    EQUALS = "="


@attrs.define(frozen=True, repr=False, eq=False)
class HashMap:
    label: str
    operation: Operation
    focal_length: int | None

    def __hash__(self):
        return self.hash

    @cached_property
    def hash(self) -> int:
        return Day15.calculate_hash(self.label)

    def __eq__(self, other: HashMap | str) -> bool:
        if isinstance(other, str):
            return self.label == other
        elif isinstance(other, HashMap):
            return self.label == other.label

    def __repr__(self) -> str:
        return f"{self.label} {self.focal_length}"


class Day15:
    @staticmethod
    def calculate_hash(word: str) -> int:
        """Calculate a hash"""
        value = 0
        for char in word:
            value += ord(char)
            value = value * 17
            value %= 256
        return value


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(self.calculate_hash(part) for part in input_data.strip().split(","))


class Day15PartB(Day15, FileReaderSolution):

    @staticmethod
    def create_instruction(label: str) -> HashMap:
        """Split a label into it's parts"""
        # Split label into parts, separated with = or -.
        # Will retain the split character due to capture group
        parts = re.split(r"([=\-])", label)
        if parts[2]:
            focal_length = int(parts[2])
        else:
            focal_length = None
        return HashMap(
            label=parts[0], operation=Operation(parts[1]), focal_length=focal_length
        )

    def solve(self, input_data: str) -> int:
        operations = [
            self.create_instruction(part) for part in input_data.strip().split(",")
        ]

        # Create 256 empty boxes, starting with 0
        boxes: list[list[HashMap]] = [[] for n in range(256)]
        for operation in operations:
            if (
                operation.operation == Operation.EQUALS
                and operation.label not in boxes[operation.hash]
            ):
                # If there is not already a lens in the box with the same label, add
                # the lens to the box immediately behind any lenses already in the box.
                # Don't move any of the other lenses when you do this. If there aren't
                # any lenses in the box, the new lens goes all the way to the front of
                # the box.
                boxes[operation.hash].append(operation)
            elif (
                operation.operation == Operation.EQUALS
                and operation.label in boxes[operation.hash]
            ):
                # If there is already a lens in the box with the same label, replace
                # the old lens with the new lens: remove the old lens and put the new
                # lens in its place, not moving any other lenses in the box.
                idx = boxes[operation.hash].index(operation)
                boxes[operation.hash][idx] = operation

            elif operation.operation == Operation.DASH:
                # If the operation character is a dash (-), go to the relevant box and
                # remove the lens with the given label if it is present in the box.
                try:
                    boxes[operation.hash].remove(operation)
                except ValueError:
                    pass

        # Calculate the resulting focusing power
        power = 0
        for box_number, box in enumerate(boxes, start=1):
            for slot, lens in enumerate(box, start=1):
                power += box_number * slot * lens.focal_length
        return power
