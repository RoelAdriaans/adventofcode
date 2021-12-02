from adventofcode2021.utils.abstract import FileReaderSolution


class Day02:
    pass


class Day02PartA(Day02, FileReaderSolution):
    MAPPING = {
        "up": (-1, 0),
        "down": (1, 0),
        "forward": (0, 1),
    }

    def solve(self, input_data: str) -> int:
        depth = position = 0
        for line in input_data.split("\n"):
            if not line:
                continue
            direction, movement = line.split(" ")[0], int(line.split(" ")[1])
            d_depth, d_movement = self.MAPPING[direction]
            depth += d_depth * movement
            position += d_movement * movement
        return depth * position


class Day02PartB(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        depth = position = aim = 0

        for line in input_data.split("\n"):
            if not line:
                continue

            direction, movement = line.split(" ")[0], int(line.split(" ")[1])

            if direction == "down":
                aim += movement
            elif direction == "up":
                aim -= movement
            else:
                position += movement
                depth += movement * aim
        return depth * position
