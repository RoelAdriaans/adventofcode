from adventofcode2022.utils.abstract import FileReaderSolution
from adventofcode2022.utils.point import XYPoint as Point


class Day09:
    moves: list[tuple[str, int]]

    def parse(self, input_data: str):
        self.moves = []
        for line in input_data.splitlines():
            p = line.split(" ")
            self.moves.append((p[0], int(p[1])))

    def simulate(self) -> int:
        tail_positions: set[tuple[int, int]] = set()

        head = Point(0, 0)
        tail = Point(0, 0)
        tail_positions.add((tail.x, tail.y))
        for move, steps in self.moves:
            for n in range(steps):
                if move == "R":
                    head.x += 1
                elif move == "L":
                    head.x -= 1
                elif move == "D":
                    head.y -= 1
                elif move == "U":
                    head.y += 1

                # Define steps for the tail to move:
                horizontal_move = head.x == tail.x or head.y == tail.y
                if horizontal_move and tail.x > head.x and tail.y == head.y:
                    tail.x -= 1
                elif horizontal_move and tail.x < head.x and tail.y == head.y:
                    tail.x += 1
                elif horizontal_move and tail.y > head.y and tail.x == head.x:
                    tail.y -= 1
                elif horizontal_move and tail.y < head.y and tail.x == head.x:
                    tail.y += 1
                elif not horizontal_move and tail.x > head.x and tail.y > head.y:
                    tail.x += 1
                    tail.y += 1
                elif not horizontal_move and tail.x > head.x and tail.y < head.y:
                    tail.x += 1
                    tail.y -= 1
                elif not horizontal_move and tail.x < head.x and tail.y > head.y:
                    tail.x -= 1
                    tail.y -= 1
                elif not horizontal_move and tail.x < head.x and tail.y < head.y:
                    tail.x += 1
                    tail.y -= 1

                tail_positions.add((tail.x, tail.y))
        return len(tail_positions)

class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.simulate()


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
