import pytest

from adventofcode2021.day16 import Day16PartB


class TestDay16PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("C200B40A82", 3),  # (1+2)
            ("04005AC33890", 54),  # (6*9)
            ("880086C3E88112", 7),  # min(7,8,9)
            ("CE00C43D881120", 9),  # max(7,8,9)
            ("D8005AC2A8F0", 1),  # 5 < 15
            ("F600BC2D8F", 0),  # 5 > 15
            ("9C005AC2F8F0", 0),  # 5 != 15
            ("9C0141080250320F1802104A08", 1),  # (1 + 3) == (2 * 2)
        ],
    )
    def test_day16b_solve(self, input_data, expected_result):
        solution = Day16PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day16b_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartB()
        res = solution("day_16/day16.txt")
        assert res == 299227024091
