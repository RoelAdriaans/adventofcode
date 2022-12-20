from __future__ import annotations

from collections import deque

from adventofcode2022.utils.abstract import FileReaderSolution


class Pair:
    left: Packet
    right: Packet

    def __init__(self, left: Packet, right: Packet):
        self.left = left
        self.right = right

    def is_valid(self) -> bool:
        """Validate if a packet is has valid pairs"""
        return False


class Packet:
    parent: Packet
    left: Packet
    right: Packet
    content: list[int]

    def __init__(self, left: Packet = None, right: Packet = None, content=None):
        self.left = left
        self.right = right
        if content is None:
            self.content = []
        else:
            self.content = content

    def __repr__(self):
        if len(self.content) > 1:
            return ",".join(str(i) for i in self.content)

        left = repr(self.left) if self.left else None
        right = repr(self.right) if self.right else None
        if left and right:
            return f"[{left},{right}]"
        else:
            return f"[{left or right}]"


class Day13:
    def parse(self, queue: deque[str]) -> Packet:
        if queue[0] == "[":
            # Remove [
            queue.popleft()
            left = self.parse(queue)
            # Remove ]
            queue.popleft()
            right = self.parse(queue)
            # Remove ]
            queue.popleft()

            # Create a new Packet
            new_packet = Packet(left=left, right=right)
            left.parent = new_packet
            right.parent = new_packet
            return new_packet
        else:
            # Next digit is one, or more, numbers
            digits = []
            while queue:
                current_digit = []
                while queue[0].isdigit():
                    current_digit.append(queue.popleft())
                if current_digit:
                    digit = int("".join(map(str, current_digit)))
                    digits.append(digit)

                if queue[0] == "]":
                    # We have reached the end of the digits
                    break
                if queue[0] == ",":
                    queue.popleft()

            return Packet(content=digits)


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        pairs: list[Pair] = []

        for input_pair in input_data.split("\n\n"):
            left = Packet(self.parse(deque(input_pair[0])))
            right = Packet(self.parse(deque(input_pair[1])))
            pair = Pair(left=left, right=right)
            pairs.append(pair)

        valid_pairs = sum(p.is_valid() for p in pairs)

        return valid_pairs


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
