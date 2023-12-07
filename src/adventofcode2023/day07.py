from __future__ import annotations

from collections import Counter
from enum import Enum

import attr
import attrs

from adventofcode.utils.abstract import FileReaderSolution


@attr.define(frozen=True, order=True)
class Bid:
    hand: Hand
    bid: int


class Score(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


@attrs.frozen
class Hand:
    # Comparing documentation:
    # https://www.attrs.org/en/stable/comparison.html#custom-comparison
    cards: str

    def score(self) -> Score:
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
        counter = Counter(self.cards)
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

        raise ValueError(f"Unknown Score for cards: {self.cards}")


class Day07:
    pass


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        bids = [
            Bid(Hand(line.split()[0]), int(line.split()[1]))
            for line in input_data.splitlines()
        ]
        total = 0
        for idx, bid in enumerate(sorted(bids), start=1):
            score = bid.bid * idx
            total += score

        return score


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
