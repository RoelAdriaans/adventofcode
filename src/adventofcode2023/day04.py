from collections import Counter

import attrs
from adventofcodeutils.parsing import extract_digits_from_string

from adventofcode.utils.abstract import FileReaderSolution


@attrs.define
class Card:
    cardnr: int
    winning_numbers: set[int]
    numbers_have: set[int]

    @classmethod
    def from_string(cls, input_string: str) -> Card:
        # Split on |
        winning_part, have_part = input_string.split("|")
        cardnr = extract_digits_from_string(winning_part)[0]
        winning = extract_digits_from_string(winning_part)[1:]
        have = extract_digits_from_string(have_part)

        return cls(cardnr, set(winning), set(have))

    def matches(self) -> int:
        return len(self.numbers_have & self.winning_numbers)

    def score(self) -> int:
        matches = self.matches()
        if matches <= 1:
            return matches
        # 1 for the first match, then doubled three times for each of the three
        # matches after the first).
        score = 1
        for _ in range(matches - 1):
            score += score
        return score


class Day04:
    pass


class Day04PartA(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        cards = [Card.from_string(line) for line in input_data.splitlines()]
        return sum([card.score() for card in cards])


class Day04PartB(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        cards = [Card.from_string(line) for line in input_data.splitlines()]
        card_matches = [(card.cardnr, card.matches()) for card in cards]
        card_counter = Counter()

        # Prime the counter, we need at least 1 of every card
        for n in range(len(cards)):
            card_counter[n + 1] = 1

        for cardnr, matches in card_matches:
            for n in range(matches):
                multiplier = card_counter[cardnr]
                card_counter[n + cardnr + 1] += multiplier

        return sum(card_counter.values())
