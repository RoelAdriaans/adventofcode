from adventofcode.utils.abstract import FileReaderSolution


class Day03:
    @staticmethod
    def char_to_value(char) -> int:
        if char.isupper():
            value = ord(char) - ord("A") + 27
        else:
            value = ord(char) - ord("a") + 1
        return value


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        total_value = 0
        for line in input_data.splitlines():
            values = [self.char_to_value(char) for char in line]

            # Split in half
            first = set(values[: len(values) // 2])
            second = set(values[len(values) // 2 :])
            difference = first.intersection(second)
            total_value += difference.pop()

        return total_value


class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        total_value = 0

        for n in range(0, len(lines), 3):
            first = {self.char_to_value(char) for char in lines[n]}
            second = {self.char_to_value(char) for char in lines[n + 1]}
            third = {self.char_to_value(char) for char in lines[n + 2]}
            difference = first.intersection(second).intersection(third)
            total_value += difference.pop()

        return total_value
