import pytest

from adventofcode2018.day01 import Day1PartB


class TestDay01PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("+1 -2 +3 +1 +1 -2", 2),
            ("+1 -1", 0),
            ("+3 +3 +4 -2 -4", 10),
            ("-6 +3 +8 +5 -6", 5),
            ("+7 +7 -2 -7 -4", 14),
        ],
    )
    def test_day01_b(self, input_data, expected_result):
        d1 = Day1PartB()
        res = d1.solve(input_data)
        assert expected_result == res

    def test_day01_data(self):
        """Result we got when we did the real solution"""
        d1 = Day1PartB()
        res = d1("day01/day_01_part01.txt")

        assert res == 75749
