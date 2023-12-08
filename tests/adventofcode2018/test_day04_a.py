import random

import pytest

from adventofcode2018.day04 import Day4PartA


class TestDay04PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (
                "[1518-11-01 00:00] Guard #10 begins shift",
                {
                    "month": 11,
                    "day": 1,
                    "hour": 0,
                    "minute": 0,
                    "mode": "guard",
                    "guard": 10,
                },
            ),
            (
                "[1518-11-01 00:05] falls asleep",
                {
                    "month": 11,
                    "day": 1,
                    "hour": 0,
                    "minute": 5,
                    "mode": "asleep",
                    "guard": False,
                },
            ),
        ],
    )
    def test_split_line_into_sections(self, input_data, expected_result):
        solution = Day4PartA()
        result = solution.split_line_into_sections(input_data)
        assert expected_result == result

    def test_split_invalid_line_into_sections(self):
        input_data = "[1518-11-01 xx:xx] Guard #10 ends shift"
        solution = Day4PartA()
        with pytest.raises(ValueError):
            solution.split_line_into_sections(input_data)

    test_data = [
        "[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up",
    ]

    def test_04a_solve(self):
        solution = Day4PartA()
        # Because our input is shuffled, we do the same here.
        shuffled_test_data = self.test_data.copy()
        random.shuffle(shuffled_test_data)
        input_data = "\n".join(shuffled_test_data)
        result = solution.solve(input_data)
        assert result == 240

    def test_day04a_data(self):
        """Result we got when we did the real solution"""
        solution = Day4PartA()
        res = solution("day04/day_04.txt")
        assert res == 87681
