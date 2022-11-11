from __future__ import annotations

import functools
import math
from collections import deque

from adventofcode2021.utils.abstract import FileReaderSolution
from adventofcode2021.utils.priority_queue import PriorityQueue


class Snail:
    value: int
    left: Snail
    right: Snail
    parent: Snail

    def __init__(self, value: int | None = None, left=None, right=None, parent=None):
        self.value = value  # type: ignore
        self.left = left
        self.right = right
        self.parent = parent

    @property
    def has_value(self):
        return self.left is None and self.right is None

    def __repr__(self):
        if self.has_value:
            return str(self.value)
        left = repr(self.left) if self.left else None
        right = repr(self.right) if self.right else None
        if left and right:
            return f"[{left},{right}]"
        else:
            return f"[{left or right}]"

    def __add__(self, other) -> Snail:
        new = Snail(left=self, right=other)
        self.parent = new
        other.parent = new
        return new

    def __lt__(self, other: Snail):
        if self.has_value and other.has_value:
            return self.value < other.value  # type: ignore
        else:
            return False

    def find_deepest_snail(self, n: int = 0) -> tuple[Snail | None, int]:
        """Find the first snail at level nested inside 4 pairs"""
        if n >= 5:
            if self.has_value:
                return self.parent, n
            else:
                return self, n

        if self.left:
            left_snail, left_value = self.left.find_deepest_snail(n + 1)
        else:
            left_snail, left_value = None, 0
        if self.right:
            right_snail, right_value = self.right.find_deepest_snail(n + 1)
        else:
            right_snail, right_value = None, 0

        if right_value > left_value:
            return right_snail, right_value
        else:
            return left_snail, left_value

    def find_splittable(self) -> Snail | None:
        if self.has_value and self.value >= 10:  # type: ignore
            return self

        if self.left:
            left_snail = self.left.find_splittable()
        else:
            left_snail = None
        if self.right:
            right_snail = self.right.find_splittable()
        else:
            right_snail = None

        if left_snail:
            return left_snail
        else:
            return right_snail


class Day18:
    def create_tree(self, line) -> Snail:
        queue = deque(line)
        root_node = self.parse(queue)
        return root_node

    def parse(self, queue: deque[str]) -> Snail:
        """Create a nested structure of snails from a dequeue of lists"""

        if queue[0] == "[":
            # Remove [
            queue.popleft()
            left = self.parse(queue)
            # Remove ,
            queue.popleft()
            right = self.parse(queue)
            # Remove ]
            queue.popleft()
            new_snail = Snail(left=left, right=right)
            left.parent = new_snail
            right.parent = new_snail
            return new_snail
        else:
            # Next digit is a number. We assume that we only have single digits number
            # in the input.
            digits = []
            while queue[0].isdigit():
                digits.append(queue.popleft())
            return Snail(value=int("".join(map(str, digits))))

    def explode(self, root_node: Snail) -> Snail:
        """Explode a snail"""
        # The root snail will explode:
        deepest, depth = Snail.find_deepest_snail(root_node)
        if not deepest:
            # Nothing to explode anymore
            raise StopIteration
        right_value = deepest.right.value
        left_value = deepest.left.value
        # Copying C# :)
        # https://github.com/VSZM/Advent_Of_Code/blob/master/2021/AOC2021/Day18.cs
        q: PriorityQueue[tuple[int, Snail]] = PriorityQueue()
        visited: set[Snail] = set()

        q.push((3, deepest.parent))  # type: ignore
        visited.add(deepest)
        path_to_root = []

        current = deepest
        while current:
            path_to_root.append(current)
            current = current.parent

        while not q.empty:
            _, node = q.pop()
            if node in visited:
                continue
            visited.add(node)

            if node.has_value:
                node.value += left_value
                break

            if node.right and node not in path_to_root and node.right not in visited:
                q.push((1, node.right))
            if node.left and node.left not in visited:
                q.push((2, node.left))
            if node.parent is not None and node.parent not in visited:
                q.push((3, node.parent))

        # Explode to the right
        q = PriorityQueue()
        visited = set()

        q.push((3, deepest.parent))  # type: ignore
        visited.add(deepest)

        while not q.empty:
            _, node = q.pop()
            if node in visited:
                continue
            visited.add(node)

            if node.has_value:
                node.value += right_value
                break

            if node.left and node not in path_to_root and node.left not in visited:
                q.push((1, node.left))
            if node.right and node.right not in visited:
                q.push((2, node.right))
            if node.parent is not None and node.parent not in visited:
                q.push((3, node.parent))

        # And remove the exploded node
        deepest.value = 0
        deepest.right = None  # type: ignore
        deepest.left = None  # type: ignore
        return root_node

    def split(self, node: Snail) -> Snail:
        """Split the snails.
        If any regular number is 10 or greater, the leftmost such regular number splits.
        """
        splittable = node.find_splittable()
        if not splittable:
            raise StopIteration

        value = splittable.value
        left = math.floor(value / 2)
        right = math.ceil(value / 2)
        left_snail = Snail(value=left, parent=splittable)
        right_snail = Snail(value=right, parent=splittable)

        splittable.value = None  # type: ignore
        splittable.left = left_snail
        splittable.right = right_snail

        return node

    def reduce(self, snail1: Snail, snail2: Snail) -> Snail:
        """Add and then reduce the snails"""
        super_snail = snail1 + snail2

        did_explode = True
        did_split = True
        while did_explode or did_split:
            try:
                self.explode(super_snail)
                did_explode = True
                continue
            except StopIteration:
                did_explode = False
            try:
                self.split(super_snail)
                did_split = True
                continue
            except StopIteration:
                did_split = False
        return super_snail

    def magnitude(self, snail: Snail) -> int:
        if snail.has_value:
            return snail.value

        left = self.magnitude(snail.left) * 3
        right = self.magnitude(snail.right) * 2

        return left + right


class Day18PartA(Day18, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        snails = [self.create_tree(line) for line in input_data.splitlines()]
        result = functools.reduce(self.reduce, snails)
        magnitude = self.magnitude(result)
        return magnitude


class Day18PartB(Day18, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        combinations = ((x, y) for x in lines for y in lines)
        max_value = 0
        for snail1_str, snail2_str in combinations:
            snail1 = self.create_tree(snail1_str)
            snail2 = self.create_tree(snail2_str)

            result = self.reduce(snail1, snail2)
            magnitude = self.magnitude(result)
            if magnitude > max_value:
                max_value = magnitude

        return max_value
