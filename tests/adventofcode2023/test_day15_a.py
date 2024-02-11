import pytest

from adventofcode2023.day15 import Day15PartA


class TestDay15PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("HASH", 52),
            ("rn=1", 30),
            ("cm-", 253),
            ("qp=3", 97),
            ("ot=7", 231),
        ],
    )
    def test_day15a_hash(self, input_data, expected_result):
        hash_value = Day15PartA.calculate_hash(input_data)
        assert hash_value == expected_result

    def test_day15a_testdata(self, testdata):
        solution = Day15PartA()
        result = solution.solve(testdata)
        assert result == 1320

    def test_day15a_data(self):
        """Result we got when we did the real solution"""
        solution = Day15PartA()
        res = solution("day_15/day15.txt")
        assert res == 507291
