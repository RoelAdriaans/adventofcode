from __future__ import annotations

from ast import literal_eval

from adventofcode2022.utils.abstract import FileReaderSolution

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
        return self._compare(self.left, self.right) == 1

    def _compare(self, left: Packet | int, right: Packet | int) -> int:
        # Convert to list if needed
        if isinstance(right, int) and isinstance(left, int):
            if left < right:
                # Right Order
                return 1
            if left == right:
                # Same, continue checking
                return 0
            if left > right:
                # Not right
                return -1

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
                return -1

            res = self._compare(left_value, right_value)
            if res != 0:
                return res

        # All the values are the same, we have to dive deeper
        if len(left) == len(right):
            # Left and right arrays are the same length, and we did not find
            # any wrong digits. Return 0 to contue comparing
            return 0
        # If the left list runs out of items first, the inputs are in
        # the right order
        if len(left) < len(right):
            return 1

        # If we are here, and all has failed, just return 0
        return 0


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
        raise NotImplementedError
