from adventofcode2021.day06 import Day06PartB


class TestDay06PartB:
    def test_day06b_solve(self):
        test_data = "3,4,3,1,2"
        solution = Day06PartB()
        result = solution.solve(test_data)
        assert result == 26984457539

    def test_day06b_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartB()
        res = solution("day_06/day06.txt")
        assert res == 1682576647495
