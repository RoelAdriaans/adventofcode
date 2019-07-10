import pytest

from solutions.day01 import Day1


class Test_Day01:
    @pytest.mark.parametrize(
        "input_data,expected_result",
        [("+1 -2 +3 +1", 3), ("+1 +1 +1", 3), ("+1 +1 -2", 0), ("-1 -2 -3", -6)],
    )
    def test_day01(self, input_data, expected_result):
        d1 = Day1()
        res = d1.solve_01(input_data)
        assert expected_result == res
