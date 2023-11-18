from adventofcode2022.utils.abstract import FileReaderSolution


class Day01:
    pass


class Day01PartA(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        elfs = input_data.split("\n\n")
        max_calories = 0
        for elf in elfs:
            total = sum([int(line) for line in elf.splitlines()])
            max_calories = max(max_calories, total)
        return max_calories


class Day01PartB(Day01, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        elfs = input_data.split("\n\n")
        max_calories = []
        for elf in elfs:
            total = sum([int(line) for line in elf.splitlines()])
            max_calories.append(total)
        max_calories.sort()
        return sum(max_calories[-3:])
