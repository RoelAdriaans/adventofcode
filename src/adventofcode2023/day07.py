from __future__ import annotations

import functools
import logging
from collections import Counter
from collections.abc import Callable
from enum import Enum

from adventofcode.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


class Score(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


@functools.total_ordering
class Hand:
    cards: str
    bid: int

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid

    @property
    def score(self) -> Score:
        return self._calculate_score(self.cards)

    @staticmethod
    def _calculate_score(cards: str) -> Score:
        """Compute the sore for this hand.
        This score can then be used for comparing cards against each other.

        In the order:
        - Five of a kind -> 7 points
        - Four of a kind -> 6 points
        - Full house -> 5
        - Three of a kind -> 4
        - Two Pair -> 3
        - One pair -> 2
        - High card -> 1
        """
        counter = Counter(cards)
        most_common = counter.most_common()
        unique_cards = len(counter)

        # Five of a kind, where all five cards have the same label
        if len(counter) == 1:
            return Score.FIVE_OF_A_KIND

        # Four of a kind, where four cards have the same label and one card has a
        # different label
        if unique_cards == 2 and most_common[0][1] == 4 and most_common[1][1] == 1:
            return Score.FOUR_OF_A_KIND

        # Full house, where three cards have the same label,
        # and the remaining two cards share a different label
        if unique_cards == 2 and most_common[0][1] == 3 and most_common[1][1] == 2:
            return Score.FULL_HOUSE

        # Three of a kind, where three cards have the same label,
        # and the remaining two cards are each different from any other card in the hand
        if (
            unique_cards == 3
            and most_common[0][1] == 3
            and most_common[1][1] == 1
            and most_common[2][1] == 1
        ):
            return Score.THREE_OF_A_KIND

        # Two pair, where two cards share one label,
        # two other cards share a second label, and the remaining card has a third label
        if (
            unique_cards == 3
            and most_common[0][1] == 2
            and most_common[1][1] == 2
            and most_common[2][1] == 1
        ):
            return Score.TWO_PAIR

        # One pair, where two cards share one label,
        # and the other three cards have a different label from the pair and each other
        if (
            unique_cards == 4
            and most_common[0][1] == 2
            and most_common[1][1] == 1
            and most_common[2][1] == 1
            and most_common[3][1] == 1
        ):
            return Score.ONE_PAIR
        # High card, where all cards' labels are distinct: 23456
        if len(counter) == 5:
            return Score.HIGH_CARD

        raise ValueError(f"Unknown Score for cards: {cards}")

    @staticmethod
    def letter_to_score(letter: str) -> int:
        scores = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
        }
        try:
            return scores[letter]
        except KeyError:
            return int(letter)

    def __repr__(self):
        return f"<Hand {self.cards} (Score: {self.score}, bid: {self.bid})>"

    def __eq__(self, other):
        if not isinstance(other, Hand):
            raise ValueError("Can't compare, must be a Hand")
        if self.cards == other.cards and self.score == other.score:
            return True
        else:
            return False

    def __lt__(self, other) -> bool:
        if self.score != other.score:
            return self.score.value < other.score.value
        else:
            for c, r in zip(self.cards, other.cards):
                if c == r:
                    continue
                else:
                    return self.letter_to_score(c) < self.letter_to_score(r)
            return False


class JokerHand(Hand):
    """New rule with Jokers!"""

    @staticmethod
    def letter_to_score(letter: str) -> int:
        if letter == "J":
            return 1
        else:
            return Hand.letter_to_score(letter)

    @staticmethod
    def find_indexes(string, search):
        return [i for i, ltr in enumerate(string) if ltr == search]

    def _calculate_score(self, cards: str) -> Score:
        """Calculate the score, but then with a joker in it!"""
        # What to to:
        # I want to replace the Jokers to create the strongest card
        # What if: I just replace the jokers with A, K Q, T, ... 2
        # and calculate the highest score?
        jokers = self.find_indexes(self.cards, "J")

        if len(jokers) == 0:
            # If there are no jokers, don't replace
            return Hand._calculate_score(cards)

        if len(jokers) == 5:
            # JJJJJ Lucky hand!
            return Score(7)

        max_score = 0
        for replacement in ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"):
            test_card = cards.replace("J", replacement)
            score = Hand._calculate_score(test_card)
            if score.value > max_score:
                max_score = score.value
        logger.debug("For cards %s, score %s", cards, max_score)
        return Score(max_score)


class Day07:
    def generic_solve(self, input_data: str, hand: Callable) -> int:
        hands = sorted(
            [
                hand(line.split()[0], int(line.split()[1]))
                for line in input_data.splitlines()
            ]
        )
        total = 0
        for idx, bid in enumerate(hands, start=1):
            score = bid.bid * idx
            total += score
        return total


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.generic_solve(input_data, Hand)


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.generic_solve(input_data, JokerHand)
