from adventofcode2021.day21 import Day21PartB


class TestDay21PartA:
    def test_day21a_solve(self):
        start_data = """\
        Player 1 starting position: 4
        Player 2 starting position: 8
        """

        solution = Day21PartB()
        result = solution.solve(start_data)
        assert result == 444356092776315

    def test_day21a_data(self):
        """Result we got when we did the real solution"""
        solution = Day21PartB()
        res = solution("day_21/day21.txt")
        assert res == 106768284484217
