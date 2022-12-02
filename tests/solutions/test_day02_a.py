from adventofcode2022.solutions.day02 import Day02PartA


class TestDay02PartA:
    def test_day02a_solve(self):
        test_data = "A Y\nB X\nC Z\n"
        solution = Day02PartA()
        result = solution.solve(test_data)
        assert result == 15

    def test_day02a_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartA()
        res = solution("day_02/day02.txt")
        assert res == 10404
