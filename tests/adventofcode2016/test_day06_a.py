from adventofcode2016.day06 import Day06PartA


class TestDay06PartA:
    def test_day06a_solve(self, testdata):
        solution = Day06PartA()
        result = solution.solve(testdata)
        assert result == "easter"

    def test_day06a_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartA()
        res = solution("day_06/day06.txt")
        assert res == "mshjnduc"
