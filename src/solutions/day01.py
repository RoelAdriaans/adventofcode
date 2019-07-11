class Day1PartA:
    def solve(self, input_data: str) -> int:
        parts = input_data.split()
        total = 0
        for part in parts:
            if part[0] == "+":
                total += int(part[1:])
            if part[0] == "-":
                total -= int(part[1:])
        return total

    def __call__(self, input_file: str) -> int:
        """
        Give the input_file as parameter, process this and return the result
        """
        with open(input_file) as f:
            input_data = f.read()
            res = self.solve(input_data=input_data)
            return res


class Day1_b:
    def solve(self, input_data: str) -> None:
        return None

    def __call__(self, input_file: str) -> int:
        """
        Give the input_file as parameter, process this and return the result
        """
        with open(input_file) as f:
            input_data = f.read()
            res = self.solve(input_data=input_data)
            return res
