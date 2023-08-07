from __future__ import annotations

import itertools

from adventofcodeutils.generic_search import BFS
from adventofcodeutils.node import Node

from adventofcode2016.utils.abstract import FileReaderSolution


class FacilityState:
    """Current state of the facility"""

    floors: list[list[str]]
    all_objects: list[str]

    def __init__(self, floors: list[list[str]]) -> None:
        """Create a new state of the Facility.

        Args:
            floors: All th objects on floors
        """
        self.floors = floors
        self.all_objects = list(itertools.chain(*floors))

    def goal_test(self) -> bool:
        """Validate that we are in the end-state, and that this is a legal setting."""
        return self.is_legal and set(self.floors[4]) == set(self.all_objects)

    @property
    def is_legal(self) -> bool:
        """Is this state legal?"""
        return True

    def __str__(self) -> str:
        ret = []
        for idx, floor in enumerate(self.floors):
            ret.append(f"F{idx} ")

    @staticmethod
    def str_element(element:str) -> str:
        """Create a short-form for an element"""
        if element == "elevator":
            return "E "
        parts = element.split()
        return f"{parts[0][0].upper()}{parts[-1][0].upper()}"

class Day11:
    pass


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
