import pytest

from adventofcode2016.day16 import Day16PartA


class TestDay16PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("1", "100"),
            ("0", "001"),
            ("11111", "11111000000"),
            ("111100001010", "1111000010100101011110000"),
        ],
    )
    def test_perform_curve(self, input_data, expected_result):
        assert Day16PartA.perform_curve(input_data) == expected_result

    def test_checksum(self):
        assert Day16PartA.calculate_checksum("110010110100") == "100"

    def test_day16a_solve(self):
        solution = Day16PartA()
        result = solution.fill_disk(start_value="10000", length=20)
        assert result == "01100"

    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == "10010101010011101"
