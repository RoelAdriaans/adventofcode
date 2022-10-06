from adventofcode2021.solutions.day11 import Day11PartB


class TestDay11PartB:
    def test_day11b_solve(self):
        start_condition = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

        solution = Day11PartB()
        result = solution.solve(start_condition)
        assert result == 195

    def test_day11b_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartB()
        res = solution("day_11/day11.txt")
        assert res == 368
