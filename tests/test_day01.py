import pytest

from solutions.day01 import Day1

# [("+1, +1, +1", 3), ("+1, +1, -2", 0), ("-1, -2, -3", -6)],


class Test_Day01:
    @pytest.mark.parametrize(
        "input_data,expected_result", [("+1, +1, +1", 3)]
    )
    def test_day01(self, input_data, expected_result):
        d1 = Day1()
        res = d1.solve_01(input_data)
        assert expected_result == res

    def test_day01_will_fail(self):
        d1 = Day1()
        res = d1.solve_01("2=3=34=45")
        assert 4 == res
