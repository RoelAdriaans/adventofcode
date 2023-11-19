from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Iterator
from functools import cache

from adventofcodeutils.node import Node
from adventofcodeutils.priority_queue import PriorityQueue

from adventofcode2021.utils.abstract import FileReaderSolution

Point = tuple[int, int]


class Day15(ABC):
    cave: dict[Point, int]

    def fill_cave(self, input_data: list[str]):
        self.cave = {}
        for x, row in enumerate(input_data):
            for y, value in enumerate(row):
                self.cave[x, y] = int(value)

    def repr_cave(self) -> str:
        lines = []
        for x in range(0, self.max_x + 1):
            lines.append(
                "".join(str(self.cave[x, y]) for y in range(0, self.max_y + 1))
            )
        return "\n".join(lines)

    @property
    @abstractmethod
    def max_x(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def max_y(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_value(self, x: int, y: int) -> int:
        """Return the value at a location."""
        raise NotImplementedError

    def find_astar(self):
        initial: Point = (0, 0)
        goal: Point = (self.max_y, self.max_y)
        path = self.astar(
            initial=initial,
            goal=goal,
        )
        return path

    def astar(
        self,
        initial: Point,
        goal: Point,
    ) -> Node[Point] | None:
        # frontier is where we've yet to go
        frontier: PriorityQueue[Node[Point]] = PriorityQueue()
        # Create the first node. Setting the cost to 0, since we will not count
        # this node in the path.
        frontier.push(Node(initial, None, cost=0.0))

        # explored is where we've been
        explored: dict[Point, float] = {initial: 0.0}

        # keep going while there is more to explore
        while not frontier.empty:
            current_node: Node[Point] = frontier.pop()
            current_state: Point = current_node.state
            # if we found the goal, we're done
            if current_state == goal:
                return current_node

            # check where we can go next and haven't explored
            for child in self._get_neighbours(*current_state):
                child_value = self.get_value(*child)

                new_cost: float = current_node.cost + child_value

                if child not in explored or explored[child] > new_cost:
                    explored[child] = new_cost
                    frontier.push(Node(child, current_node, new_cost))
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

    def solve(self, input_data: str) -> int:
        self.fill_cave(input_data.splitlines())
        # The path should have the total cost from start to end
        path = self.find_astar()
        return int(path.cost)


class Day15PartA(Day15, FileReaderSolution):
    def get_value(self, x: int, y: int) -> int:
        return self.cave[x, y]

    @property
    @cache  # type: ignore
    def max_y(self) -> int:
        return max(y for _, y in self.cave)

    @property
    @cache  # type: ignore
    def max_x(self) -> int:
        return max(x for x, _ in self.cave)


class Day15PartB(Day15, FileReaderSolution):
    def get_value(self, x: int, y: int) -> int:
        multiplier = self.real_max_x + 1
        mod_x = x % multiplier
        mod_y = y % multiplier

        delta_x = x // multiplier
        delta_y = y // multiplier

        old_value = self.cave[mod_x, mod_y]
        quadrant = delta_x + delta_y
        new_value = quadrant + old_value
        # Wrap around when 10 or higher
        if new_value >= 10:
            new_value -= 9
        return new_value

    @property
    @cache  # type: ignore
    def real_max_x(self) -> int:
        return max(x for x, _ in self.cave)

    @property
    @cache  # type: ignore
    def real_max_y(self) -> int:
        return max(y for _, y in self.cave)

    @property
    @cache  # type: ignore
    def max_x(self) -> int:
        return (max(x for x, _ in self.cave) + 1) * 5 - 1

    @property
    @cache  # type: ignore
    def max_y(self) -> int:
        return (max(y for _, y in self.cave) + 1) * 5 - 1
