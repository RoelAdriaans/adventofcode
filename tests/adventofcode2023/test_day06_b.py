from adventofcode2023.day06 import Day06PartB


class TestDay06PartB:
    def test_day06b_testdata(self, testdata):
        solution = Day06PartB()
        result = solution.solve(testdata)
        assert result == 71503

    def test_day06b_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == 28545089
