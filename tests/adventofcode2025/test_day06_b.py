from adventofcode2025.day06 import Day06PartB


class TestDay06PartB:
    def test_day06b_testdata(self, testdata):
        solution = Day06PartB()
        result = solution.solve(testdata)
        assert result == 3263827

    def test_day06b_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == 9077004354241
