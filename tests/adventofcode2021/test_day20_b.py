from adventofcode2021.day20 import Day20PartB


class TestDay20PartB:
    def test_day20b_solve(self, testdata):
        solution = Day20PartB()
        result = solution.solve(testdata)
        assert result == 3351

    def test_day20b_data(self):
        """Result we got when we did the real solution"""
        solution = Day20PartB()
        res = solution("day_20/day20.txt")
        assert res == 16793
