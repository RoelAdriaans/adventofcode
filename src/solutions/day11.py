from utils.abstract import FileReaderSolution


class Day11:
    def __init__(self, size: int = 300):
        self.grid = []
        self.size = size

    @staticmethod
    def computer_power_level(x: int, y: int, serial: int) -> int:
        """
        Compute the powerlevel of this cell at position `x, y` with serial `serial`
        """
        rack_id = x + 10
        powerlevel = rack_id * y
        powerlevel += serial
        powerlevel *= rack_id
        powerlevel_str = "{:06d}".format(powerlevel)

        hunderdth = int(str(powerlevel_str)[-3])
        hunderdth -= 5
        return hunderdth

    def generate_grid(self, serial):
        self.grid = [
            [self.computer_power_level(x, y, serial) for y in range(0, self.size + 1)]
            for x in range(0, self.size + 1)
        ]

    def compute_summed_area(self):
        for y in range(0, self.size + 1):
            for x in range(0, self.size + 1):
                # i(x,y) + I(x,y-1) + I(x-1,y) - I(x-1, y-1)

                if x > 0 and y > 0:
                    value = (
                        self.grid[x][y]
                        + self.grid[x][y - 1]
                        + self.grid[x - 1][y]
                        - self.grid[x - 1][y - 1]
                    )
                elif x > 0:
                    value = self.grid[x][y] + self.grid[x - 1][y]
                elif y > 0:
                    value = self.grid[x][y] + self.grid[x][y - 1]
                else:
                    value = self.grid[x][y]

                self.grid[x][y] = value

    def sum_area(self, tl_x: int, tl_y: int, rb_x: int, rb_y: int) -> int:
        """
        Compute the sum of an area
        with the points in a square.
        tl = top left, rb is bottom right
        tl_x,tl_y

                    rb_x,rb_y
        """
        # result is now sum of elements
        # between (0, 0) and (rb_x, rb_y)
        if max([tl_x, tl_y, rb_x, rb_y]) > self.size:
            return -1
        res = self.grid[rb_x][rb_y]

        # Remove elements between (0, 0)and (tl_x-1, rb_y)
        if tl_x > 0:
            res = res - self.grid[tl_x - 1][rb_y]

        # Remove elements between (0, 0) and (rb_x, tl_y-1)
        if tl_y > 0:
            res = res - self.grid[rb_x][tl_y - 1]

        # Add self.grid[tl_x-1][tl_y-1] as elements
        # between (0, 0) and (tl_x-1, tl_y-1) are subtracted twice
        if tl_x > 0 and tl_y > 0:
            res = res + self.grid[tl_x - 1][tl_y - 1]
        return res

    def compute_from(self, x: int, y: int, size: int = 3) -> int:
        """ Compute an 3x3 area, with x, y as top-left"""
        tl_x = x
        tl_y = y
        rb_x = x + (size - 1)
        rb_y = y + (size - 1)
        res = self.sum_area(tl_x, tl_y, rb_x, rb_y)
        return res

    def print_partial_grid(self, top_x, top_y):
        print()
        for y in range(top_y - 1, top_y + 4):
            for x in range(top_x - 1, top_x + 4):
                value = "{:3d} ".format(self.grid[x][y])
                print(value, end="")
            print()

    def find_best_grid(self, grid_size: int = 3):
        most_power = float("-inf")
        grid_with_power = None
        for y in range(1, self.size - 1):
            for x in range(1, self.size - 1):
                compute_power = self.compute_from(x, y, grid_size)
                if compute_power > most_power:
                    grid_with_power = (x, y)
                    most_power = compute_power
        return grid_with_power, most_power

    def find_best_grid_size(self):
        most_power = float("-inf")
        best_grid = None
        best_grid_size = None
        # grid_size_to_test = self.size - 1
        grid_size_to_test = int(self.size / 4)
        for size in range(1, grid_size_to_test):
            grid, power = self.find_best_grid(size)
            if power > most_power:
                most_power = power
                best_grid = grid
                best_grid_size = size
        return {
            "best_grid": best_grid,
            "most_power": most_power,
            "best_grid_size": best_grid_size,
        }


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        serial = int(input_data)
        self.generate_grid(serial)
        self.compute_summed_area()
        res, power = self.find_best_grid()
        return str(res)


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        serial = int(input_data)
        self.generate_grid(serial)
        self.compute_summed_area()
        res = self.find_best_grid_size()
        return f"{res['best_grid'][0]}, {res['best_grid'][1]}, {res['best_grid_size']}"
