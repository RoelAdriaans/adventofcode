from adventofcode2021.solutions.day03 import Day03PartB


class TestDay03PartB:
    def test_day03b_solve(self):
        test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
        solution = Day03PartB()
        result = solution.solve(test_data)
        assert result == 230

    def test_day03b_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartB()
        res = solution("day_03/day03.txt")
        assert res == 7928162
