import itertools
from collections import Counter
from collections.abc import Iterator
from functools import cache

from adventofcode2021.utils.abstract import FileReaderSolution


class Day21:
    @staticmethod
    def modulo(n: int) -> int:
        return ((n - 1) % 10) + 1

    @staticmethod
    def dice() -> Iterator[int]:
        for n in itertools.count(start=1):
            yield ((n - 1) % 100) + 1

    def run_loops(self, location_1: int, location_2: int) -> int:
        score_1, score_2 = 0, 0
        dice = self.dice()
        player_1 = True
        for n in itertools.count(start=1):
            throw = sum([next(dice) for n in range(3)])
            if player_1:
                location_1 = self.modulo(location_1 + throw)
                score_1 += location_1
            else:
                location_2 = self.modulo(location_2 + throw)
                score_2 += location_2

            # And switch players
            player_1 = not player_1

            # Have we won yet?
            if score_1 >= 1000:
                return score_2 * (n * 3)
            elif score_2 >= 1000:
                return score_1 * (n * 3)

        raise ValueError("Infinity ended and no score was found.")


class Day21PartA(Day21, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        start_1 = int(lines[0][-1])
        start_2 = int(lines[1][-1])
        return self.run_loops(start_1, start_2)


class Day21PartB(Day21, FileReaderSolution):
    cnt: Counter[int]

    @cache
    def find_wins(
        self, location_1: int, score_1: int, location_2: int, score_2: int
    ) -> tuple[int, int]:
        wins_1 = wins_2 = 0
        for throw, multiplier in self.cnt.items():
            new_1 = self.modulo(location_1 + throw)
            new_1_score = score_1 + new_1
            if new_1_score >= 21:
                wins_1 += multiplier
            else:
                tmp_2_wins, tmp_1_wins = self.find_wins(
                    location_2, score_2, new_1, new_1_score
                )
                wins_1 += tmp_1_wins * multiplier
                wins_2 += tmp_2_wins * multiplier
        return wins_1, wins_2

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        start_1 = int(lines[0][-1])
        start_2 = int(lines[1][-1])

        # Pre-compute the throws and the number of times it can happen
        options = (1, 2, 3)
        self.cnt = Counter(
            sum(pt) for pt in itertools.product(options, options, options)
        )
        p1, p2 = self.find_wins(start_1, 0, start_2, 0)
        return max(p1, p2)
