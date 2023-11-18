from adventofcode2022.solutions.day14 import Day14PartA


class TestDay14PartA:
    def test_day14a_solve(self, testdata):
        solution = Day14PartA()
        result = solution.solve(testdata)
        assert result == 24

    def test_day14a_data(self):
        """Result we got when we did the real solution"""
        solution = Day14PartA()
        res = solution("day_14/day14.txt")
        assert res == 885
