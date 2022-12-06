from adventofcode2022.utils.abstract import FileReaderSolution


class Day06:
    pass


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        input_data = input_data.strip()
        for start in range(0, len(input_data)):
            packet = input_data[start : start + 4]
            if len(set(packet)) != 4:
                # Duplicated characters
                continue
            # We have something new, return starting position + 4 chars in this packet
            return start + 4

        return -1


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
