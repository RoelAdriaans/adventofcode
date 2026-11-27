import math
from itertools import combinations

import attrs
from adventofcodeutils import parsing

from adventofcode.utils.abstract import FileReaderSolution


@attrs.define
class Junction:
    x: int
    y: int
    z: int

    def distance(self, other: Junction):
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )


class Day08:
    @staticmethod
    def create_junction_boxes(input_data: str) -> list[Junction]:
        return [
            Junction(*parsing.extract_digits_from_string(line))
            for line in input_data.splitlines()
        ]

    def create_sorted_junctions(self, boxes: list[Junction]) -> list[list]:
        pairs = []
        for box1, box2 in combinations(boxes, 2):
            distance = box1.distance(box2)
            pairs.append((box1, box2, distance))

        # Sort the pairs of junctions
        pairs.sort(key=lambda x: x[2])
        return pairs


@attrs.define
class Circuit:
    # junctions: Junction, Junction, distance
    junctions: list

    # boxes, all the boxes in this circuit
    boxes: set

    def add_circuit(self, circuit: list):
        self.circuits.append(circuit)
        self.boxes.add(circuit[0])
        self.boxes.add(circuit[1])


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        boxes = Day08PartA.create_junction_boxes(input_data)
        junctions = self.create_sorted_junctions(boxes)
        circuits = []
        used_boxes = set()
        for junction in junctions[:1000]:
            # Check if the junction is already in one of the circuits
            if junction[0] or junction[1] in used_boxes:
                ...
            else:
                # Not yet in use, new circuit
                c = Circuit(junctions=[junction], boxes={junction[0], junction[1]})

        # Sort

        # Return product of top 3 size


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
