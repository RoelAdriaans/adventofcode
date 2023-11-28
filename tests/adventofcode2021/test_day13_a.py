import pytest

from adventofcode2021.day13 import Day13PartA

test_small_data = """0,0
1,1
2,2
3,3
4,4
6,4
7,3
8,2
9,1
10,0
4,1
6,1
1,10

fold along y=5
"""

test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


class TestDay13PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (test_small_data, 13),
            (test_data, 17),
        ],
    )
    def test_day13a_solve(self, input_data, expected_result):
        solution = Day13PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day13a_two_folds(self):
        solution = Day13PartA()
        result = solution.solve(test_data)
        assert result == 17

        # To another fold
        solution.start_folding(loops=1)

        # And after the second loop, we should have 16 left
        assert solution.count_dots() == 16

    def test_day13a_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res < 903
        assert res > 661
        assert res == 753
