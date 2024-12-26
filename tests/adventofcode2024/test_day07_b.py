from adventofcode2024.day07 import Day07PartB


class TestDay07PartB:
    def test_day07b_testdata(self, testdata):
        solution = Day07PartB()
        result = solution.solve(testdata)
        assert result == 11387

    def test_day07b_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartB()
        res = solution("day_07/day07.txt")
        assert res == 227615740238334
