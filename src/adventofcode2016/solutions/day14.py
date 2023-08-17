from __future__ import annotations

import hashlib
import logging
import re

from adventofcode2016.utils.abstract import FileReaderSolution

# Following regex will match 3 OR more matches
three_char = re.compile(r"(\w)\1{2,}")


class Day14:
    def get_five_match(self, salt: str, start_index: int, letter: str) -> int:
        """Validate the next 1.000 hashes after `start_index` to validate
        if it's a match"""
        five_char = re.compile(r"(" + letter + r")\1{4,}")

        for n in range(start_index, start_index + 1001):
            character = f"{salt}{n}"
            pad_hash = hashlib.md5(character.encode()).hexdigest()
            if five_char.search(pad_hash):
                # Match found!
                return n
        # Not found
        raise ValueError

    def get_md5(self, salt: str, index: int) -> bool:
        character = f"{salt}{index}"
        pad_hash = hashlib.md5(character.encode()).hexdigest()

        if match := three_char.search(pad_hash):
            # Find in the next 1.000 hashes
            letter = match[0][0]
            try:
                # Find for the next matches. We start at index + 1,
                # otherwise we will match ourselves :)
                self.get_five_match(salt, index + 1, letter)
                logging.debug(
                    "Found match: 5 letter match in index %s, letter %s", index, letter
                )
                return True
            except ValueError:
                return False


class Day14PartA(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        current_index = 0
        matches = 0
        while matches < 64:
            if self.get_md5(input_data.strip(), current_index):
                matches += 1
                logging.debug(
                    "Found match on index %s, match nr %s", current_index, matches
                )

            current_index += 1
        return current_index - 1


class Day14PartB(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
