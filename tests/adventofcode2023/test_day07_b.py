import pytest

from adventofcode2023.day07 import Day07PartB, JokerHand, Score


class TestDay07PartB:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("32T3K", Score.ONE_PAIR),
            ("KK677", Score.TWO_PAIR),
            ("T55J5", Score.FOUR_OF_A_KIND),
            ("KTJJT", Score.FOUR_OF_A_KIND),
            ("QQQJA", Score.FOUR_OF_A_KIND),
            ("QJJQ2", Score.FOUR_OF_A_KIND),
            ("8JJJ4", Score.FOUR_OF_A_KIND),
        ],
    )
    def test_day07a_test_hand_score(self, input_data, expected_result):
        hand = JokerHand(input_data, 0)
        assert hand.score == expected_result

    def test_day07b_testdata(self, testdata):
        solution = Day07PartB()
        result = solution.solve(testdata)
        assert result == 5905

    def test_day07b_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartB()
        res = solution("day_07/day07.txt")
        assert res == 251824095
