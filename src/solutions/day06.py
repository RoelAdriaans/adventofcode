from utils.abstract import FileReaderSolution
from collections import Counter, namedtuple

Point = namedtuple("Point", "x y id")


class Day06:
    grid = None
    points = {}
    max_x = 0
    max_y = 0

    def yield_over_grid(self, extra=0):
        for y in range(0, self.max_y + extra):
            for x in range(0, self.max_x + extra):
                yield x, y

    def generate_points(self, input_string):
        """ Generate a grid based on the input string. """
        id = 1
        for line in input_string:
            x, y = line.split(",")
            x = int(x)
            y = int(y)
            new_point = Point(x=x, y=y, id=id)
            self.points[id] = new_point
            id += 1

        self.max_x = max([p.x for p in self.points.values()])
        self.max_y = max([p.y for p in self.points.values()])

    def generate_grid(self):
        """
        Generate a grid based on the points in `self.grid`
        """
        self.grid = dict()
        for x in range(0, self.max_x + 5):
            self.grid[x] = dict()
            for y in range(0, self.max_y + 5):
                self.grid[x][y] = False

        for point in self.points.values():
            self.grid[point.x][point.y] = point

    def print_grid(self):
        """ Print the grid to the standard output."""
        print()
        for y in range(0, self.max_y + 5):
            for x in range(0, self.max_x + 5):
                if self.grid[x][y]:
                    char = self.grid[x][y].id + 64
                    print(chr(char), end="")
                else:
                    print(".", end="")
            print()

    def generate_distance(self):
        """
        For every point in the grid, locate the closest point using
        Manhattan distance.
        """
        for x, y in self.yield_over_grid(extra=5):
            if self.grid[x][y] is not False:
                # Skip grids that are already filled in
                continue
            # Loop over every point in the grid, and compute the closest point
            test_point = Point(x=x, y=y, id=0)
            closest_point = self.compute_closest_point(test_point)
            if closest_point:
                self.grid[x][y] = closest_point

    def compute_closest_point(self, point: Point) -> [Point, bool]:
        """
        For Point `point`, return the closest point. If multiple points
        have the same closest distance, we return False
        """
        min_distance = self.max_x + self.max_y
        min_point = False
        for test_point in self.points.values():
            distance = self.compute_distance(
                point.x, point.y, test_point.x, test_point.y
            )
            if min_point and distance == min_distance:
                # We already multiple claims for this distance.
                # If we don't get a distance that is lower that the current one, we set
                # the closest point to None. If we then find a closer point we return
                # that point, or we return false.
                min_point = False

            if distance < min_distance:
                min_distance = distance
                min_point = test_point

        return min_point

    def compute_biggest_area(self) -> int:
        """
        Compute the number of points of the biggest area

        Loop over the grid, and add points to the Point Counter.
        If a point connects to the edge of out grid, it's infinite and we ignore this
        point.
        :return:
        """
        # Loop over the grid, and do stuff;
        point_cnt = Counter()
        for id, value in self.points.items():
            point_cnt[id] = 0

        for x, y in self.yield_over_grid(extra=1):
            point = self.grid[x][y]
            if point:
                if (x == 0) or (y == 0) or (x == self.max_x) or (y == self.max_y):
                    # We are on the edge, exclude this point;
                    point_cnt[point.id] = False
                elif point_cnt[point.id] is not False:
                    point_cnt[point.id] += 1

        # Return the biggest area
        return point_cnt.most_common(1)[0][1]

    @staticmethod
    def compute_distance(a: int, b: int, x: int, y: int) -> int:
        """
        Compute the Manhattan distance between points (a, b) and (x, y)
        """
        res = abs(a - x) + abs(b - y)
        return res


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        input_lines = input_data.split("\n")
        self.generate_points(input_lines)
        self.generate_grid()
        self.generate_distance()
        result = self.compute_biggest_area()
        return result


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
