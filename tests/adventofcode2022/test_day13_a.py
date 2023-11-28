import pytest

from adventofcode2022.day13 import Day13PartA


class TestDay13PartA:
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
    def test_day13a_individual_pairs(self, testdata, pair, valid):
        pairs = testdata.split("\n\n")

        solution = Day13PartA()
        result = solution.solve(pairs[pair - 1])
        assert result == valid

    def test_day13a_solve(self, testdata):
        solution = Day13PartA()
        result = solution.solve(testdata)
        assert result == 13

    def test_day13a_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartA()
        res = solution("day_13/day13.txt")
        assert res > 1008
        assert res > 3364
        assert res != 5738
        assert res < 7750
        assert res == 6420
