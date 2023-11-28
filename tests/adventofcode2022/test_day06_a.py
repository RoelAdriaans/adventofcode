import pytest

from adventofcode2022.day06 import Day06PartA


class TestDay06PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
        ],
    )
    def test_day06a_solve(self, input_data, expected_result):
        solution = Day06PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day06a_data(self):
        """Result we got when we did the real solution"""
        solution = Day06PartA()
        res = solution("day_06/day06.txt")
        assert res == 1566
