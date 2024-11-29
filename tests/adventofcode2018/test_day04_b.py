import random

from adventofcode2018.day04 import Day4PartB


class TestDay04PartA:
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

    def test_04b_solve(self):
        solution = Day4PartB()
        # Because our input is shuffled, we do the same here.
        shuffled_test_data = self.test_data.copy()
        random.shuffle(shuffled_test_data)
        input_data = "\n".join(shuffled_test_data)
        result = solution.solve(input_data)
        assert result == 4455

    def test_day04b_data(self):
        """Result we got when we did the real solution"""
        solution = Day4PartB()
        res = solution("day_04/day04.txt")
        assert res == 136461
