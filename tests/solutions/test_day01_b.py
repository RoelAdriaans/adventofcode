from adventofcode2021.solutions.day01 import Day01PartB


class TestDay01PartB:
    def test_day01b_solve(self):
        test_data = """199
200
208
210
200
207
240
269
260
263"""

        solution = Day01PartB()
        result = solution.solve(test_data)
        assert result == 5

    def test_day01b_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartB()
        res = solution("day_01/day01.txt")
        assert res == 1797
