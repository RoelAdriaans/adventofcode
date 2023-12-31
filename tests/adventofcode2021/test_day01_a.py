from adventofcode2021.day01 import Day01PartA


class TestDay01PartA:
    def test_day01a_solve(self):
        test_data = """199
200
208
210
200
207
240
269
260
263
"""
        solution = Day01PartA()
        result = solution.solve(test_data)
        assert result == 7

    def test_day01a_data(self):
        """Result we got when we did the real solution"""
        solution = Day01PartA()
        res = solution("day_01/day01.txt")
        assert res == 1766
