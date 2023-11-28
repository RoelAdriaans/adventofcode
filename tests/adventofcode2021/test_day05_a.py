from adventofcode2021.day05 import Day05PartA


class TestDay05PartA:
    def test_day05a_solve(self):
        test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
        solution = Day05PartA()
        result = solution.solve(test_input)
        assert result == 5

    def test_day05a_data(self):
        """Result we got when we did the real solution"""
        solution = Day05PartA()
        res = solution("day_05/day05.txt")
        assert res == 5306
