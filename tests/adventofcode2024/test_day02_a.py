from adventofcode2024.day02 import Day02PartA


class TestDay02PartA:
    def test_day02a_testdata(self, testdata):
        solution = Day02PartA()
        result = solution.solve(testdata)
        assert result == 2

    def test_day02a_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartA()
        res = solution("day_02/day02.txt")
        assert res == 390
