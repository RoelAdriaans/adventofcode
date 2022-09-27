from adventofcode2021.utils.abstract import FileReaderSolution


class Day08:
    @staticmethod
    def parse(input_string: str) -> tuple[list[str], list[str]]:
        """
        Parse the input string into two components:
        - The 10 patterns we see
        - Four digit of output Value
        """
        patterns, output_value = input_string.split(" | ")
        return patterns.split(), output_value.split()


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        # Map a signal to the number of lines. Eg, number 7 uses 3 segments
        patterns = [self.parse(line) for line in input_data.splitlines() if line]

        accepted_values = (2, 4, 3, 7)

        result = [
            len(value) in accepted_values
            for pattern in patterns
            for value in pattern[1]
        ]
        return sum(result)


class Day08PartB(Day08, FileReaderSolution):
    def compute_sum(self, input_line) -> int:
        return int("".join([str(x) for x in self.compute_digits(input_line)]))

    def compute_digits(self, input_line) -> list[int]:
        patterns, values = self.parse(input_line)
        mapping = self.map(patterns)

        total = []
        for value in values:
            value = "".join(sorted(value))
            total.append(mapping[value])
        return total

    def map(self, patterns) -> dict[str, int]:
        """
        Try to reverse engineer the mapping on this line, and return the sum
        of the digits
        """
        # Store every unique pattern we see, and remove them after we matched
        pattern_set = {"".join(sorted(v)) for v in patterns}

        # Store the total mapping, this will contain letters -> Digit, eg:
        # {"bcdf": 4, acdfg": 3}
        mapping = {}

        # First pick the easy values
        # Map the length of the pattern to the digit, eg map "ba", length 2 to 1.
        easy_map = {
            2: 1,
            4: 4,
            3: 7,
            7: 8,
        }
        for pattern in pattern_set.copy():
            if digit := easy_map.get(len(pattern)):
                mapping[pattern] = digit
                pattern_set.discard(pattern)

        # I know that 6 is everything EXCEPT one of 1's numbers.
        # That can only be one:
        # Mapping for 1 is:
        mapping_one = self.find_mapping_for_digit(mapping, 1)
        mapping_four = self.find_mapping_for_digit(mapping, 4)
        for pattern in pattern_set.copy():
            if len(pattern) == 6:
                left_over = (set("abcdefg") - set(pattern)).pop()
                if left_over in mapping_one:
                    mapping[pattern] = 6
                    pattern_set.discard(pattern)

                # Mapping for 9 is length(6) with pattern with 4:
                if all([letter in list(pattern) for letter in list(mapping_four)]):
                    mapping[pattern] = 9
                    pattern_set.discard(pattern)

        # After this, the only item left with 6 characters is 0
        for pattern in pattern_set.copy():
            if len(pattern) == 6:
                mapping[pattern] = 0
                pattern_set.discard(pattern)

        # Mapping for 3 is length(5) with pattern for one enabled
        for pattern in pattern_set.copy():
            if len(pattern) == 5:
                # if mapping_one in pattern:
                if all([letter in list(pattern) for letter in list(mapping_one)]):
                    mapping[pattern] = 3
                    pattern_set.discard(pattern)
                    break

        # Only 5 and 2 left.
        # The digit that is OFF in the 6, must be ON in the 2.
        mapping_six = self.find_mapping_for_digit(mapping, 6)
        six_off = (set("abcdefg") - set(mapping_six)).pop()

        for pattern in pattern_set.copy():
            if six_off in pattern:
                mapping[pattern] = 2
                pattern_set.discard(pattern)
                break

        # Only 5 left
        mapping[pattern_set.pop()] = 5
        if len(pattern_set) != 0:
            raise ValueError(f"Unmapped patterns left: {pattern_set}")

        return mapping

    @staticmethod
    def find_mapping_for_digit(mapping: dict, needle: int) -> str:
        """In the dict `mapping`, find the key for `needle`"""

        for key, value in mapping.items():
            if needle == value:
                return key
        else:
            raise ValueError(f"Key {needle} not found")

    def solve(self, input_data: str) -> int:
        """Where we really have to map, and stop counting :)"""

        totals = [self.compute_sum(line) for line in input_data.splitlines() if line]
        return sum(totals)
