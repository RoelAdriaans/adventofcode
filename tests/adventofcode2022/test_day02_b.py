from adventofcode2022.day02 import Day02PartB


class TestDay02PartB:
    def test_day02b_solve(self):
        test_data = "A Y\nB X\nC Z\n"
        solution = Day02PartB()
        result = solution.solve(test_data)
        assert result == 12

    def test_day02b_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartB()
        res = solution("day_02/day02.txt")
        assert res == 10334
