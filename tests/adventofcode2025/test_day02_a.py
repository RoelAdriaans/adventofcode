import pytest

from adventofcode2025.day02 import Day02PartA


class TestDay02PartA:
    def test_day02a_testdata(self, testdata):
        solution = Day02PartA()
        result = solution.solve(testdata)
        assert result == 1227775554

    @pytest.mark.parametrize(
        ("id_to_test, is_valid"),
        [
            (11, False),
            (22, False),
            (55, False),
            (6464, False),
            (123123, False),
            (1188511885, False),
            (123, True),
            (456, True),
        ],
    )
    def test_invalid_ids(self, id_to_test, is_valid):
        assert Day02PartA.test_valid_id(id_to_test) == is_valid

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("11-22", 33),
            ("95-115", 99),
            ("11-22,95-115", 33 + 99),
        ],
    )
    def test_day02a_solve(self, input_data, expected_result):
        solution = Day02PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day02a_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartA()
        res = solution("day_02/day02.txt")
        assert res == 40055209690
