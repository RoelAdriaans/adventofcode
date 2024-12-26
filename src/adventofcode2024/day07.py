from __future__ import annotations

from adventofcodeutils import parsing

from adventofcode.utils.abstract import FileReaderSolution


class Day07:
    concatenation: bool = False

    def validate(self, test_value: int, digits_left: list[int]):
        if len(digits_left) == 1 and digits_left[0] == test_value:
            return True
        if len(digits_left) == 1:
            return False
        if digits_left[0] > test_value:
            return False

        left = digits_left.pop()
        right = digits_left.pop()

        score_mul = left * right
        score_add = left + right

        if self.validate(test_value, digits_left[:] + [score_mul]):
            return True
        if self.validate(test_value, digits_left[:] + [score_add]):
            return True

        if self.concatenation:
            score_concat = int(str(left) + str(right))
            if self.validate(test_value, digits_left[:] + [score_concat]):
                return True

        return False

    def validate_equation(self, line) -> int:
        """Returns the total value of this equation if it's valid, otherwise 0"""
        test_value, *digits = parsing.extract_digits_from_string(line)
        digits = list(reversed(digits))
        if self.validate(test_value, digits_left=digits):
            return test_value
        return 0


class Day07PartA(Day07, FileReaderSolution):
    concatenation = False

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        return sum(self.validate_equation(line) for line in lines)


class Day07PartB(Day07, FileReaderSolution):
    concatenation = True

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        return sum(self.validate_equation(line) for line in lines)
