from adventofcode2022.solutions.day11 import Day11PartB


class TestDay11PartB:
    def test_day11b_solve(self, testdata):
        solution = Day11PartB()
        result = solution.solve(testdata)
        assert result == 2713310158

    def test_day11b_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartB()
        res = solution("day_11/day11.txt")
        assert res == 21816744824
