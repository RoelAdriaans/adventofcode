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
                    head.y += 1
                elif move == "U":
                    head.y -= 1

                # Define steps for the tail to move:
                horizontal_move = head.x == tail.x or head.y == tail.y
                if tail.distance(head)== 1:
                    pass
                elif horizontal_move and tail.x > head.x and tail.y == head.y:
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
                self.print(head, tail, tail_positions)

        return len(tail_positions)

    @staticmethod
    def print(head: Point, tail: Point, tail_positions: set[tuple[int, int]]):
        min_x = min(head.x, tail.x)
        min_y = min(head.y, tail.y)
        max_x = max(head.x, tail.x)
        max_y = max(head.y, tail.y)
        line = "\n\n"
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                pnt = Point(x, y)
                if head == tail == pnt:
                    line += "*"
                elif head == pnt and head != tail:
                    line += "H"
                elif tail == pnt and head != tail:
                    line += "T"
                elif (x, y) in tail_positions:
                    line += "#"
                else:
                    line += "."
            line += "\n"
        line += "\n\n"
        print(line)


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.simulate()


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
