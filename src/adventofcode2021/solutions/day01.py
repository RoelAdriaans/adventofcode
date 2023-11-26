from adventofcode.utils.abstract import FileReaderSolution


class Day01:
    pass


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        num_changes = 0
        depths = [int(n) for n in input_data.split("\n") if n]
        last_number = depths[0]
        for depth in depths:
            if depth > last_number:
                num_changes += 1
            last_number = depth
        return num_changes


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        depths = [int(n) for n in input_data.split("\n") if n]

        total_difference = 0

        for idx in range(len(depths)):
            a = depths[idx : idx + 3]
            b = depths[idx + 1 : idx + 4]
            if sum(a) < sum(b):
                total_difference += 1

        return total_difference
