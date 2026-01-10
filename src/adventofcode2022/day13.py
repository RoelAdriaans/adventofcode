from ast import literal_eval
from functools import cmp_to_key

from adventofcode.utils.abstract import FileReaderSolution

Packet = list[int | list]


class Pair:
    left: Packet
    right: Packet
    index: int

    def __init__(self, left: Packet, right: Packet, index: int):
        self.left = left
        self.right = right
        self.index = index

    def is_valid(self) -> bool:
        """Validate if a packet is has valid pairs"""
        return self.compare(self.left, self.right) < 0

    @classmethod
    def compare(cls, left: Packet | int, right: Packet | int) -> int:
        # Convert to list if needed
        if isinstance(right, int) and isinstance(left, int):
            return left - right
        if isinstance(left, int):
            left = [left]
        if isinstance(right, int):
            right = [right]

        # Let's dive into this! left and right have now both been turned
        # into lists
        for idx, left_value in enumerate(left):
            try:
                right_value = right[idx]
            except IndexError:
                # Until now, all the values have been the same.
                # Right side ran out of items,
                # so inputs are not in the right order
                return 1

            res = cls.compare(left_value, right_value)
            if res != 0:
                return res

        return len(left) - len(right)


class Day13:
    def parse(self, string_pair: str, index: int) -> Pair:
        p1, p2 = string_pair.splitlines()
        left: Packet = literal_eval(p1)
        right: Packet = literal_eval(p2)

        return Pair(left=left, right=right, index=index)


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        pairs: list[Pair] = []

        for index, input_pair in enumerate(input_data.split("\n\n"), start=1):
            pairs.append(self.parse(input_pair, index))

        valid_pairs = sum(p.index for p in pairs if p.is_valid())

        return valid_pairs


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        pairs: list[Pair] = []

        for index, input_pair in enumerate(input_data.split("\n\n"), start=1):
            pairs.append(self.parse(input_pair, index))

        # Add the divider packets:
        divider_packets = "[[2]]\n[[6]]"
        pairs.append(self.parse(divider_packets, 0))

        # Now, extract all the packets into a list:
        packets = [p.left for p in pairs] + [p.right for p in pairs]

        sorted_packets = sorted(packets, key=cmp_to_key(Pair.compare))
        i1 = sorted_packets.index([[2]]) + 1
        i2 = sorted_packets.index([[6]]) + 1
        return i1 * i2
