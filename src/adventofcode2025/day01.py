from adventofcode.utils.abstract import FileReaderSolution


class Day01:
    pass


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        pointer = 50
        number_zero = 0
        for line in input_data.splitlines():
            direction = line[0]
            number = int(line[1:])
            if direction == "L":
                pointer = (pointer - number) % 100
            else:
                pointer = (pointer + number) % 100
            if pointer == 0:
                number_zero += 1
        return number_zero


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        pointer = 50
        number_zero = 0
        for line in input_data.splitlines():
            direction = line[0]
            number = int(line[1:])
            if direction == "L":
                direction = -1
            else:
                direction = 1
            # Going to brute force this
            for i in range(number):
                pointer = (pointer + direction) % 100
                if pointer == 0:
                    number_zero += 1

        return number_zero
