from adventofcode2016.solutions.day06 import Day06PartB


class TestDay06PartB:
    def test_day06b_solve(self, testdata):
        solution = Day06PartB()
        result = solution.solve(testdata)
        assert result == "advent"

    def test_day06b_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == "apfeeebz"
