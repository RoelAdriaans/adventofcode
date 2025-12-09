from adventofcode2025.day07 import Day07PartA


class TestDay07PartA:
    def test_day07a_testdata(self, testdata):
        solution = Day07PartA()
        result = solution.solve(testdata)
        assert result == 21

    def test_day07a_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 1590
