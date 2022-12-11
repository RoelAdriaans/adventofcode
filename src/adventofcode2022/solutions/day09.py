import more_itertools

from adventofcode2022.utils.abstract import FileReaderSolution
from adventofcode2022.utils.point import XYPoint as Point


class Day09:
    moves: list[tuple[str, int]]
    tail_positions: set[tuple[int, int]]
    head: Point
    tails: list[Point]

    def parse(self, input_data: str):
        self.moves = []
        for line in input_data.splitlines():
            p = line.split(" ")
            self.moves.append((p[0], int(p[1])))

    def simulate(self, no_heads: int) -> int:
        self.tail_positions = set()

        self.head = Point(0, 0)
        self.tails = [Point(0, 0) for _ in range(no_heads)]
        self.tail_positions.add((self.tails[-1].x, self.tails[-1].y))
        for move, steps in self.moves:
            for n in range(steps):
                if move == "R":
                    self.head.x += 1
                elif move == "L":
                    self.head.x -= 1
                elif move == "D":
                    self.head.y += 1
                elif move == "U":
                    self.head.y -= 1

                # Define steps for the tails to move:
                self.move_tails()
                self.tail_positions.add((self.tails[-1].x, self.tails[-1].y))

        return len(self.tail_positions)

    def move_tails(self):
        to_move = [self.head] + self.tails
        for head, tail in more_itertools.sliding_window(to_move, 2):
            self.move_tail(head, tail)

    @staticmethod
    def move_tail(head, tail) -> Point:
        horizontal_move = head.x == tail.x or head.y == tail.y
        if horizontal_move and tail.distance(head) == 1:
            return tail
        if not horizontal_move and tail.distance(head) == 2:
            return tail
        elif horizontal_move and tail.x > head.x and tail.y == head.y:
            tail.x -= 1
        elif horizontal_move and tail.x < head.x and tail.y == head.y:
            tail.x += 1
        elif horizontal_move and tail.y > head.y and tail.x == head.x:
            tail.y -= 1
        elif horizontal_move and tail.y < head.y and tail.x == head.x:
            tail.y += 1
        elif not horizontal_move and tail.x > head.x and tail.y > head.y:
            tail.x -= 1
            tail.y -= 1
        elif not horizontal_move and tail.x > head.x and tail.y < head.y:
            tail.x -= 1
            tail.y += 1
        elif not horizontal_move and tail.x < head.x and tail.y > head.y:
            tail.x += 1
            tail.y -= 1
        elif not horizontal_move and tail.x < head.x and tail.y < head.y:
            tail.x += 1
            tail.y += 1
        return tail


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.simulate(1)


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.simulate(9)
