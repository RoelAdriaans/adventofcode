from adventofcode2023.day04 import Day04PartB


class TestDay04PartB:
    def test_day04b_testdata(self, testdata):
        solution = Day04PartB()
        result = solution.solve(testdata)
        assert result == 30

    def test_day04b_data(self):
        """Result we got when we did the real solution"""
        solution = Day04PartB()
        res = solution("day_04/day04.txt")
        assert res == 6420979
