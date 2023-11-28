from adventofcode2021.day03 import Day03PartA


class TestDay03PartA:
    def test_day03a_solve(self):
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
        solution = Day03PartA()
        result = solution.solve(test_data)
        assert result == 198

    def test_day03a_data(self):
        """Result we got when we did the real solution"""
        solution = Day03PartA()
        res = solution("day_03/day03.txt")
        assert res == 3895776
