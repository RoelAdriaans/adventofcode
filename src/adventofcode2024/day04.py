from adventofcode.utils.abstract import FileReaderSolution


class Day04:
    pass


class Day04PartA(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        counter = 0
        # Horizontal
        for line in lines:
            counter += line.count("XMAS")
            counter += line.count("SAMX")

        # Vertical
        for line in list(map(list, zip(*lines))):
            line = "".join(line)
            counter += line.count("XMAS")
            counter += line.count("SAMX")

        # Diagonal
        for h in range(len(lines)):
            for w in range(len(lines)):
                try:
                    word = (
                        lines[h][w]
                        + lines[h + 1][w + 1]
                        + lines[h + 2][w + 2]
                        + lines[h + 3][w + 3]
                    )
                    if word == "XMAS" or word == "SAMX":
                        counter += 1
                except IndexError:
                    pass
                try:
                    # Prevent wrapping around
                    if w - 3 < 0:
                        continue

                    word = (
                        lines[h][w]
                        + lines[h + 1][w - 1]
                        + lines[h + 2][w - 2]
                        + lines[h + 3][w - 3]
                    )
                    if word == "XMAS" or word == "SAMX":
                        counter += 1
                except IndexError:
                    pass
        return counter


class Day04PartB(Day04, FileReaderSolution):
    @staticmethod
    def find_x(lines, w, h) -> str:
        try:
            return "".join(
                [
                    lines[h - 1][w - 1],
                    lines[h - 1][w + 1],
                    lines[h][w],
                    lines[h + 1][w - 1],
                    lines[h + 1][w + 1],
                ]
            )
        except IndexError:
            return "QQQQQ"

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        counter = 0
        for h in range(len(lines)):
            for w in range(1, len(lines)):
                # Prevent wrapping around
                x = self.find_x(lines, w, h)
                if (
                    x[2] == "A"
                    and ((x[0] == "M" and x[4] == "S") or (x[0] == "S" and x[4] == "M"))
                    and ((x[1] == "M" and x[3] == "S") or (x[1] == "S" and x[3] == "M"))
                ):
                    counter += 1

        return counter
