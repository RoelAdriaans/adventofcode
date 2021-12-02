from adventofcode2021.utils.abstract import FileReaderSolution


class Day02:
    pass


class Day02PartA(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        depth = position = 0
        for line in [line for line in input_data.split("\n") if line]:
            direction, movement = line.split(" ")[0], int(line.split(" ")[1])

            match direction:
                case "up":
                    depth -= movement
                case "down":
                    depth += movement
                case "forward":
                    position += movement
                case _:
                    raise ValueError(f"Invalid direction value: {repr(direction)}")

        return depth * position


class Day02PartB(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        depth = position = aim = 0

        for line in [line for line in input_data.split("\n") if line]:

            direction, movement = line.split(" ")[0], int(line.split(" ")[1])
            match direction:
                case "down":
                    aim += movement
                case "up":
                    aim -= movement
                case "forward":
                    position += movement
                    depth += movement * aim
                case _:
                    raise ValueError(f"Invalid direction value: {repr(direction)}")

        return depth * position
