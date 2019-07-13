import pytest

from solutions.day01 import Day1PartA


class TestDay01PartA:
    @pytest.mark.parametrize(
        "input_data,expected_result",
        [("+1 -2 +3 +1", 3), ("+1 +1 +1", 3), ("+1 +1 -2", 0), ("-1 -2 -3", -6)],
    )
    def test_day01(self, input_data, expected_result):
        d1 = Day1PartA()
        res = d1.solve(input_data)
        assert expected_result == res

    def test_day01_data(self):
        """ Result we got when we did the real solution """
        d1 = Day1PartA()
        res = d1("data/day01/day_01_part01.txt")

        assert res == 525
