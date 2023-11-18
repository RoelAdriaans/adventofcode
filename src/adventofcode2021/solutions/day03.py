from collections import Counter

from adventofcode2021.utils.abstract import FileReaderSolution


class Day03:
    pass


class Day03PartA(Day03, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = [line for line in input_data.split("\n") if line]

        new_line = ""
        for bit in range(len(lines[0])):
            bone = bzero = 0
            for line in lines:
                val = line[bit]
                if val == "0":
                    bzero += 1
                else:
                    bone += 1
            if bone > bzero:
                new_line += "1"
            else:
                new_line += "0"

        bin_value = int(new_line, 2)
        reversed_value = new_line.replace("0", "t").replace("1", "0").replace("t", "1")
        inverted = int(reversed_value, 2)
        return bin_value * inverted


class Day03PartB(Day03, FileReaderSolution):
    @staticmethod
    def find_most_common(input_lines: list[str], n: int) -> Counter:
        """Find the most common value in the list of inputs, on bit `n`"""
        cnt: Counter = Counter()
        for line in input_lines:
            cnt[line[n]] += 1
        return cnt

    def find_value(self, bitlines, bit, hi_low: bool) -> int:
        """
        Find the value, and use bit as a tie breaker when the count is the same
        """
        # First copy the bitlines, make sure we don't modify the original value
        bitlines = bitlines.copy()
        for i in range(len(bitlines[0])):
            cnt = self.find_most_common(bitlines, i)
            if cnt["0"] == cnt["1"]:
                to_keep = bit
            else:
                if hi_low:
                    # Keep the most common bit.
                    to_keep = cnt.most_common(1)[0][0]
                else:
                    # Keep the most common bit.
                    to_keep = cnt.most_common(2)[1][0]

            new_bitlines = []
            for line in bitlines:
                if line[i] == to_keep:
                    new_bitlines.append(line)
            bitlines = new_bitlines
            if len(bitlines) == 1:
                return int(bitlines[0], 2)
        return False

    def solve(self, input_data: str) -> int:
        lines = [line for line in input_data.split("\n") if line]

        oxygen = self.find_value(lines, "1", True)
        co2 = self.find_value(lines, "0", False)

        return oxygen * co2
