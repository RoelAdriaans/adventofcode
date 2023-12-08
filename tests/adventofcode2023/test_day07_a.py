import pytest

from adventofcode2023.day07 import Day07PartA, Hand, Score


class TestDay07PartA:
    @pytest.mark.parametrize(
        ("card1", "card2", "lt", "eq"),
        [
            ("AAAAA", "AAAAA", False, True),
            ("33333", "22222", False, False),
            ("33332", "2AAAA", False, False),
            ("77888", "77788", False, False),
            ("22222", "33333", True, False),
            ("KK677", "KTJJT", False, False),
        ],
    )
    def test_day07a_cards(self, card1, card2, lt, eq):
        hand1 = Hand(card1, 100)
        hand2 = Hand(card2, 100)
        ltcompare = hand1 < hand2
        assert ltcompare == lt

        eqcompare = hand1 == hand2
        assert eqcompare == eq

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
        hand = Hand(input_data, 0)
        assert hand.score == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day07a_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res == 250946742
