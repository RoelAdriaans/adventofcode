from more_itertools import grouper

from adventofcode.utils.abstract import FileReaderSolution


class Day16:
    @staticmethod
    def perform_curve(a: str) -> str:
        """Perform modified Dragon Curve"""
        # Call the data you have at this point "a".
        # Make a copy of "a"; call this copy "b".
        # Reverse the order of the characters in "b".
        # In "b", replace all instances of 0 with 1 and all 1s with 0.
        b = a[::-1].translate(str.maketrans("01", "10"))

        # The resulting data is "a", then a single 0, then "b".
        return f"{a}0{b}"

    @staticmethod
    def calculate_checksum(input_value: str) -> str:
        first = True
        while first or len(input_value) % 2 == 0:
            first = False
            new = []
            for pairs in grouper(input_value, 2):
                if pairs[0] == pairs[1]:
                    new.append("1")
                else:
                    new.append("0")
            input_value = "".join(new)

        return input_value

    def fill_disk(self, start_value: str, length: int) -> str:
        """Fill a disk with checksum"""
        # First, calculate checksum to at least length
        while len(start_value) <= length:
            start_value = self.perform_curve(start_value)

        # We only need the first characters
        dragon = start_value[:length]
        checksum = self.calculate_checksum(dragon)

        return checksum


class Day16PartA(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        return self.fill_disk(start_value=input_data.strip(), length=272)


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        return self.fill_disk(start_value=input_data.strip(), length=35651584)
