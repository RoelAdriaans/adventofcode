from __future__ import annotations

import re
from collections import Counter

import attrs

from adventofcode2016.utils.abstract import FileReaderSolution


@attrs.define
class Room:
    """Define a room"""

    encrypted_name: str
    sector_id: int
    checksum: str

    @classmethod
    def from_string(cls, input_string: str) -> Room:
        group = re.match(r"^([\w-]*)-(\d*)\[(\w*)\]$", input_string)
        return cls(encrypted_name=group[1], sector_id=int(group[2]), checksum=group[3])

    def is_valid(self) -> bool:
        # Remove and sort the letters, ties are alphabetical
        letters = sorted(self.encrypted_name.replace("-", ""))
        name_counter = Counter(letters)
        most_common_letters = "".join(
            k[0] for k in name_counter.most_common(len(self.checksum))
        )
        return most_common_letters == self.checksum


class Day04:
    pass


class Day04PartA(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        rooms = [Room.from_string(line) for line in input_data.splitlines()]
        return sum(room.sector_id for room in rooms if room.is_valid())


class Day04PartB(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
