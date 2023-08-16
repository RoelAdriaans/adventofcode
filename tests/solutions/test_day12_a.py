from adventofcode2016.solutions.day12 import Day12PartA


class TestDay12PartA:
    def test_day12a_solve_testdata(self, testdata):
        solution = Day12PartA()
        result = solution.solve(testdata)
        assert result == 42

    def test_day12a_data(self):
        """Result we got when we did the real solution"""
        solution = Day12PartA()
        res = solution("day_12/day12.txt")
        assert res == 318003
