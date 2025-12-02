import pytest

from adventofcode2025.day02 import Day02PartB


class TestDay02PartB:
    @pytest.mark.parametrize(
        ("id_to_test, is_valid"),
        [
            (12341234, False),
            (123123123, False),
            (1212121212, False),
            (1111111, False),
            (11, False),
            (12, True),
            (21, True),
            (22, False),
            (111, False),
            (99, False),
            (100, True),
        ],
    )
    def test_invalid_ids(self, id_to_test, is_valid):
        assert Day02PartB.test_valid_id(id_to_test) == is_valid

    def test_day02b_testdata(self, testdata):
        solution = Day02PartB()
        result = solution.solve(testdata)
        assert result == 4174379265

    def test_day02b_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartB()
        res = solution("day_02/day02.txt")
        assert res == 50857215650
