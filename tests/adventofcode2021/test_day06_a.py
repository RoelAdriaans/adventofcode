from adventofcode2021.solutions.day06 import Day06PartA


class TestDay06PartA:
    def test_day06a_solve(self):
        test_data = "3,4,3,1,2"
        solution = Day06PartA()
        result = solution.solve(test_data)
        assert result == 5934

    def test_day06a_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartA()
        res = solution("day_06/day06.txt")
        assert res == 373378
