from __future__ import annotations

import math

import attrs

from adventofcode.utils.abstract import FileReaderSolution
from adventofcode.utils.parsing import extract_digits_from_string


@attrs.define(frozen=True)
class Result:
    time: int
    distance: int


class Day06:
    @staticmethod
    def parse(input_data: str, strip_spaces=False) -> list[Result]:
        lines = input_data.splitlines()
        if strip_spaces:
            lines[0] = lines[0].replace(" ", "")
            lines[1] = lines[1].replace(" ", "")
        times = extract_digits_from_string(lines[0])
        distances = extract_digits_from_string(lines[1])
        results = []
        for time, distance in zip(times, distances):
            results.append(Result(time=time, distance=distance))
        return results

    @staticmethod
    def compute_options(result: Result) -> int:
        options = 0
        for charge in range(result.time):
            # charge the boat for charge seconds
            distance = charge * (result.time - charge)
            if distance > result.distance:
                options += 1
        return options

    def find_options(self, input_data: str, bad_kerning: bool) -> int:
        times = self.parse(input_data, bad_kerning)
        return math.prod([self.compute_options(result) for result in times])


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.find_options(input_data, False)


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.find_options(input_data, True)
