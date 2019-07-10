class Day1:
    def solve_01(self, input_data: str) -> int:
        parts = input_data.split()
        total = 0
        for part in parts:
            if part[0] == "+":
                total += int(part[1:])
            if part[0] == "-":
                total -= int(part[1:])
        return total

    def __call__(self, input_data: str) -> int:
        return self.solve_01(input_data=input_data)
