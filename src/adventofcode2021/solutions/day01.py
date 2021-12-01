from adventofcode2021.utils.abstract import FileReaderSolution


class Day01:
    pass


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        num_changes = 0
        # depths = advent_utils.string_to_list_of_ints(input_data, split_string="\n")
        depths = [int(n) for n in input_data.split("\n") if n]
        last_number = depths[0]
        for depth in depths:
            if depth > last_number:
                num_changes += 1
            last_number = depth
        return num_changes


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
