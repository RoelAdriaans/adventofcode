from __future__ import annotations

import attrs
from adventofcodeutils.parsing import extract_digits_from_string

from adventofcode2016.utils.abstract import FileReaderSolution


@attrs.define
class Disc:
    number: int
    positions: int
    time: int
    start_position: int

    @classmethod
    def from_string(cls, line: str) -> Disc:
        disc, positions, time, start_position = extract_digits_from_string(line)
        return Disc(
            number=disc, positions=positions, time=time, start_position=start_position
        )

    def pos_at_time(self, time: int) -> int:
        """Position at time `time`"""
        pos = self.number + time + self.start_position
        return pos % self.positions


class Day15:
    def parse(self, input_data: str) -> list[Disc]:
        return [Disc.from_string(line) for line in input_data.splitlines()]

    def align_zero(self, discs) -> int:
        """Align until all the disks are at 0"""
        time = 0
        while True:
            positions = [disc.pos_at_time(time) for disc in discs]
            if set(positions) == {0}:
                return time
            time += 1


class Day15PartA(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        disks = self.parse(input_data)
        return self.align_zero(disks)


class Day15PartB(Day15, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        disks = self.parse(input_data)

        disks.append(
            Disc(number=len(disks) + 1, positions=11, time=0, start_position=0)
        )
        return self.align_zero(disks)
