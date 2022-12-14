from adventofcode2022.utils.abstract import FileReaderSolution
from adventofcode2022.utils.generic_search import BFS
from adventofcode2022.utils.node import Node
from adventofcode2022.utils.point import XYPoint as Point


class Day12:
    grid: dict[Point, int]
    max_x: int
    max_y: int
    start_position: Point
    end_position: Point

    def parse(self, input_lines: str):
        self.grid = {}

        for x, line in enumerate(input_lines.splitlines()):
            for y, char in enumerate(line):
                pnt = Point(x, y)
                if char == "S":
                    self.start_position = pnt
                    int_value = 0
                elif char == "E":
                    self.end_position = pnt
                    int_value = 26
                else:
                    int_value = ord(char) - ord("a") + 1
                self.grid[pnt] = int_value
        self.max_x = max(point.x for point in self.grid.keys())
        self.max_y = max(point.y for point in self.grid.keys())

    def goal_test(self, pnt: Point) -> bool:
        return pnt == self.end_position

    def heuristic(self, pnt: Point) -> float:
        distance = self.end_position.distance(pnt)
        return distance

    def neighbours(self, pnt: Point) -> list[Point]:
        neighbours = []
        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            new_point = Point(dx, dy) + pnt
            if (
                new_point.x < 0
                or new_point.y < 0
                or new_point.x > self.max_x
                or new_point.y > self.max_y
            ):
                continue
            current_value = self.grid[pnt]
            if (
                self.grid[new_point] <= current_value
                or self.grid[new_point] == current_value + 1
                or self.grid[new_point] == self.end_position
            ):
                neighbours.append(new_point)
        return neighbours


class Day12PartA(Day12, FileReaderSolution):
    def find_sortest_path(self):
        shortest_node = BFS().search(
            initial=self.start_position,
            goal_test=self.goal_test,
            successors=self.neighbours,
        )
        if shortest_node:
            path = Node.node_to_path(shortest_node)
            # Subtract the start and ending node
            return len(path) - 1
        else:
            raise ValueError("No Path found!")

    def print_path(self, path: list[Point]):
        local_grid = {}
        for pnt, value in self.grid.items():
            local_grid[pnt] = "   " + chr(value + ord("a") - 1)

        for idx, pnt in enumerate(path):
            local_grid[pnt] = f" {idx:03}"

        lines = []
        for x in range(self.max_x + 1):
            line = []
            for y in range(self.max_y + 1):
                line.append(local_grid[Point(x, y)])
            lines.append("".join(line))
        print()
        print("\n".join(lines))

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.find_sortest_path()


class Day12PartB(Day12, FileReaderSolution):
    def find_sortest_path(self):
        # Find all the possible starting positions
        start_points = [point for point, value in self.grid.items() if value == 1]
        shortest = 9999

        for point in start_points:
            shortest_node = BFS().search(
                initial=point,
                goal_test=self.goal_test,
                successors=self.neighbours,
            )

            if shortest_node:
                path = Node.node_to_path(shortest_node)
                # Subtract the start and ending node, and compute the minimum value
                shortest = min(len(path) - 1, shortest)
        return shortest

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.find_sortest_path()
