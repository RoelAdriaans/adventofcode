from more_itertools import sliding_window

from adventofcode2022.utils.abstract import FileReaderSolution


class Day06:
    @staticmethod
    def parse_packets(input_data: str, length: int) -> int:
        input_data = input_data.strip()
        for idx, packet in enumerate(sliding_window(input_data, length)):
            if len(set(packet)) != length:
                # Duplicated characters
                continue
            # We have something new, return starting position + 4 chars in this packet
            return idx + length

        raise ValueError("No package found for length %s", length)


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.parse_packets(input_data, 4)


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.parse_packets(input_data, 14)
