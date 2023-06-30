from __future__ import annotations

from collections import Counter

from adventofcode2016.utils.abstract import FileReaderSolution


class Day06:
    pass


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        lines = input_data.splitlines()
        # Transpose the list
        transposed = zip(*lines)
        res = []
        for line in transposed:
            cnt = Counter(line)
            letter = cnt.most_common(1)[0][0]
            res.append(letter)

        return "".join(res)


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
