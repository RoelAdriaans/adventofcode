from adventofcode.utils.abstract import FileReaderSolution


class Day03:
    pass


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(self.find_jotage(line) for line in input_data.splitlines())

    @classmethod
    def find_jotage(cls, input_data: str) -> int:
        """Find the highest jotage in the given input data."""
        digits = list(map(int, input_data))
        # Implement the logic to find the highest jotage
        index = 0
        max_jotage = 0

        while index < len(digits):
            for i in range(index + 1, len(digits)):
                # Loop over the digits to the right of the current index
                # If any of the
                count = digits[index] * 10 + digits[i]
                if count > max_jotage:
                    max_jotage = count
            index += 1
        return max_jotage


class Day03PartB(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(
            int("".join(self.find_jotage(line))) for line in input_data.splitlines()
        )

    @classmethod
    def find_jotage(cls, input_data: str, n: int = 12) -> str:
        """Find the highest jotage in the given input data, but with `n` batteries
        turned on"""

        if len(input_data) == n:
            return input_data

        largest_index = 0
        largest_jotage = 0
        digits = list(map(int, input_data))

        for i in range(len(input_data) - (n - 1)):
            if largest_jotage < digits[i]:
                largest_index = i
                largest_jotage = digits[i]

        remaining_batteries = input_data[largest_index + 1 :]
        jotate_str = input_data[largest_index]
        if n > 1:
            jotate_str += str(cls.find_jotage(remaining_batteries, n=n - 1))
        return jotate_str
