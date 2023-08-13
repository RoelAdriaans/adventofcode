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
        for floor in self.floors:
            generators = {
                item.split()[0] for item in floor if item.endswith("generator")
            }
            chips = {item.split()[0] for item in floor if item.endswith("chip")}

            for chip in chips:
                if not generators:
                    # No generators, nothing to check
                    break
                if chip not in generators:
                    return False

        return True

    def __str__(self) -> str:
        ret = []
        for idx, floor in enumerate(reversed(self.floors)):
            elements = " ".join(self.str_element(element) for element in floor)
            ret.append(f"F{len(self.floors) - idx} {elements}".strip())
        return "\n".join(ret)

    @staticmethod
    def str_element(element: str) -> str:
        """Create a short-form for an element"""
        if element == "elevator":
            return "ELEV"
        parts = element.split()
        return f"{parts[0][:2].upper()}{parts[-1][:2].upper()}"


class Day11:
    def parse(self, input_data: str) -> FacilityState:
        floors = []

        for line in input_data.splitlines():
            floor = []

            parts = line.split()
            name = None
            for part in parts[5:]:
                if part in ("and", ",", "a", "relevant."):
                    continue

                if name is None:
                    name = part.rstrip(",.").replace("-compatible", "").strip()
                else:
                    # We name and type:
                    floor.append(f"{name} {part.rstrip(',.').strip()}")
                    name = None

            floors.append(floor)

        # When you enter the containment area, you and the elevator will start on the
        # first floor.
        floors[0].insert(0, "elevator")

        return FacilityState(floors=floors)


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        start_state = self.parse(input_data)

        return -1


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
