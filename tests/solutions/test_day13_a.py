from collections import deque

import pytest

from adventofcode2022.solutions.day13 import Day13PartA


class TestDay13PartA:
    @pytest.mark.parametrize(
        "input_string",
        (
            "[[1,2],[3,4]]",
            # "[]",
            # "[9]",
            # "[9]",
            # "[1, 1, 3, 1, 1]",
            # "[[1],[2,3,4]]",
            # "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        ),
    )
    @pytest.mark.skip(reason="Not yet implemented")
    def test_day13a_parsing(self, input_string):
        solution = Day13PartA()
        assert repr(solution.parse(deque(input_string))) == input_string

    @pytest.mark.parametrize(
        ("pair", "valid"),
        [
            (1, True),
            (2, True),
            (3, False),
            (4, True),
            (5, False),
            (6, True),
            (7, False),
            (8, False),
        ],
    )
    @pytest.mark.skip(reason="Not yet implemented")
    def test_day13a_individual_pairs(self, testdata, pair, valid):
        pairs = testdata.split("\n\n")

        solution = Day13PartA()
        result = solution.solve(pairs[pair - 1])
        assert result == valid

    @pytest.mark.skip(reason="Not yet implemented")
    def test_day13a_solve(self, testdata):
        solution = Day13PartA()
        result = solution.solve(testdata)
        assert result == 13

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day13a_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res == 0
