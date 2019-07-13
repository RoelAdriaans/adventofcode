from utils.abstract import FileReaderSolution, SimpleSolution


class Day1PartA(FileReaderSolution):
    def solve(self, input_data: str) -> int:
        parts = input_data.split()
        total = 0
        for part in parts:
            if part[0] == "+":
                total += int(part[1:])
            if part[0] == "-":
                total -= int(part[1:])
        return total


class Day1PartB(SimpleSolution):
    def solve(self, input_data: str) -> str:
        return f"Het result van b is: {input_data.lower()}"
