from __future__ import annotations

import hashlib
import logging

import attrs

from adventofcode.utils.abstract import FileReaderSolution


@attrs.define
class MatchResult:
    hash: str
    first_code: str
    current_position: int


class Day05:
    @staticmethod
    def find_match(prefix: str, starting: int) -> MatchResult:
        """With prefix, start at a specific number. Return the value of the first
        non-zero number, and the current position"""
        position = starting
        while True:
            pos_hash = hashlib.md5(
                f"{prefix}{position}".encode(), usedforsecurity=False
            ).hexdigest()
            if pos_hash[:5] == "00000":
                return MatchResult(
                    hash=pos_hash, first_code=pos_hash[5], current_position=position
                )
            position += 1


class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        prefix = input_data.strip()
        result = []
        current_location = 0
        for _ in range(8):
            match = self.find_match(prefix, current_location)
            current_location = match.current_position + 1
            logging.debug(
                "Found digit %s at location %d",
                match.first_code,
                match.current_position,
            )
            result.append(match.first_code)

        return "".join(result)


class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        prefix = input_data.strip()
        result: list[str | None] = [None] * 8
        current_location = 0

        while not all(result):
            match = self.find_match(prefix, current_location)
            current_location = match.current_position + 1
            password_position = match.hash[5]
            password_character = match.hash[6]

            if password_position.isdigit() and int(password_position) <= 7:
                numeric_position = int(password_position)
                if not result[numeric_position]:
                    result[numeric_position] = password_character

                    logging.debug(
                        "Found digit %s at location %d, current password: %s",
                        password_character,
                        numeric_position,
                        "".join(x if x else "_" for x in result),
                    )

        logging.info("Found password after %d runs", current_location)
        return "".join(x if x else "_" for x in result)
