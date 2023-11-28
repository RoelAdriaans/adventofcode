from adventofcode2016.day14 import Day14PartA


class TestDay14PartA:
    def test_day14a_solve(self):
        solution = Day14PartA()
        result = solution.solve("abc")
        assert result == 22728

    def test_day14a_data(self):
        """Result we got when we did the real solution"""
        solution = Day14PartA()
        res = solution("day_14/day14.txt")
        assert res == 23769
