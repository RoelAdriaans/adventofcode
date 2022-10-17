from __future__ import annotations

from collections.abc import Iterator
from typing import Generic

from adventofcode2021.utils.abstract import FileReaderSolution
from adventofcode2021.utils.node import Node, T
from adventofcode2021.utils.priority_queue import PriorityQueue


class Day15(Generic[T]):
    cave: dict[tuple[int, int], int]
    max_x: int
    max_y: int

    def fill_cave(self, input_data: list[str]):
        self.cave = {}
        for x, row in enumerate(input_data):
            for y, value in enumerate(row):
                self.cave[x, y] = int(value)
        self.max_x = max(x for x, _ in self.cave)
        self.max_y = max(y for _, y in self.cave)

    def repr_cave(self) -> str:
        lines = []
        for x in range(0, self.max_x + 1):
            lines.append(
                "".join(str(self.cave[x, y]) for y in range(0, self.max_y + 1))
            )
        return "\n".join(lines)

    def find_astar(self):
        initial: T = (0, 0)
        goal: T = (self.max_y, self.max_y)
        path = self.astar(
            initial=initial,
            goal=goal,
        )
        return path

    def astar(
        self,
        initial: T,
        goal: T,
    ) -> Node[T] | None:
        # frontier is where we've yet to go
        frontier: PriorityQueue[Node[T]] = PriorityQueue()
        frontier.push(Node(initial, None, 0.0, self.cave[initial]))

        # explored is where we've been
        explored: dict[T, float] = {initial: 0.0}

        # keep going while there is more to explore
        while not frontier.empty:
            current_node: Node[T] = frontier.pop()
            current_state: T = current_node.state
            # if we found the goal, we're done
            if current_state == goal:
                return current_node

            # check where we can go next and haven't explored
            for child in self._get_neighbours(*current_state):
                new_cost: float = current_node.cost + self.cave[child]

                if child not in explored or explored[child] > new_cost:
                    explored[child] = new_cost
                    frontier.push(Node(child, current_node, new_cost, self.cave[child]))
        return None

    def _get_neighbours(self, x, y) -> Iterator[tuple[int, int]]:
        """Get a list of neighbours for this location."""
        locations = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
        ]
        for new_x, new_y in locations:
            if new_x < 0 or new_x > self.max_x:
                continue
            if new_y < 0 or new_y > self.max_y:
                continue
            yield new_x, new_y


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.fill_cave(input_data.splitlines())
        path = self.find_astar()
        locations = Node.node_to_path(path)
        values = [self.cave[x, y] for x, y in locations]
        # We skip the first location
        total = sum(values[1:])
        return total


class Day15PartB(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
