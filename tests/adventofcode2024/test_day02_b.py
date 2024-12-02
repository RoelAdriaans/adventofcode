from adventofcode2024.day02 import Day02PartB


class TestDay02PartB:
    def test_day02b_testdata(self, testdata):
        solution = Day02PartB()
        result = solution.solve(testdata)
        assert result == 4

    def test_day02b_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartB()
        res = solution("day_02/day02.txt")
        assert res != 391
        assert res == 439
