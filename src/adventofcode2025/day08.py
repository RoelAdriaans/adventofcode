import logging

from adventofcodeutils.parsing import string_to_list_of_ints
from adventofcodeutils.point import XYZPoint

from adventofcode.utils.abstract import FileReaderSolution

_logger = logging.getLogger(__name__)


class Day08:
    boxes: set[XYZPoint]

    def parse_boxes(self, input_data):
        self.boxes = set()
        for line in input_data.splitlines():
            self.boxes.add(XYZPoint(*string_to_list_of_ints(line)))

    def find_closest(self, junction: XYZPoint) -> tuple[XYZPoint, int]:
        """Find cloest point to junction, and return that point and the distance."""
        closest_point = None
        closest_distance = None
        for box in self.boxes:
            if box == junction:
                # Skip self
                continue

            distance = box.euclidean_dist(junction)

            if closest_point is None or distance < closest_distance:
                closest_point = box
                closest_distance = distance
        return closest_point, closest_distance


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str, junction_boxes: int = 1000) -> int:
        """Solve the shortest connections, with maximum junction_boxes in use"""
        self.parse_boxes(input_data)

        _logger.debug("Found %s junction boxes", len(self.boxes))

        # For each junction, find the closest other junction
        _logger.debug("Starting parsing closest junction box")
        boxes_with_distance = []
        for box in self.boxes:
            # boxes_with_distance[box] = self.find_closest(box)
            boxes_with_distance.append((box, *self.find_closest(box)))

        _logger.debug("Done parsing closest junction box")
        boxes_with_distance = sorted(boxes_with_distance, key=lambda x: x[2])

        networks = []
        current_network = []
        previous_distance = None

        for box in boxes_with_distance:
            start, destination, distance = box
            if previous_distance is None:
                previous_distance = distance
                continue
            elif previous_distance == distance:
                current_network.append(box)
            elif previous_distance != distance:
                networks.append(current_network)
                current_network = [box]
                previous_distance = distance


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
