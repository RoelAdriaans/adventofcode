import pytest

from adventofcode2023.day07 import Day07PartA, Score, Hand


class TestDay07PartA:
    def test_day07a_testdata(self, testdata):
        solution = Day07PartA()
        result = solution.solve(testdata)
        assert result == 6440

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("AAAAA", Score.FIVE_OF_A_KIND),
            ("AA8AA", Score.FOUR_OF_A_KIND),
            ("23332", Score.FULL_HOUSE),
            ("TTT98", Score.THREE_OF_A_KIND),
            ("23432", Score.TWO_PAIR),
            ("A23A4", Score.ONE_PAIR),
            ("23456", Score.HIGH_CARD),
        ],
    )
    def test_day07a_test_hand_score(self, input_data, expected_result):
        hand = Hand(input_data)
        assert hand.score() == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day07a_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 0
