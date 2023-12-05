from __future__ import annotations

import attrs
import tqdm
from adventofcodeutils.parsing import extract_digits_from_string

from adventofcode.utils.abstract import FileReaderSolution


class Seed:
    # Do need?
    ...


@attrs.define(frozen=True)
class Range:
    source: str
    destination: str

    dest_range: int
    source_range: int
    length: int


class Day05:
    seeds:list[int]
    maps:list[Range]

    def parse(self, input_data: str):
        """Parse the whole input list"""
        parts = input_data.split("\n\n")
        # Seeds
        self.seeds = extract_digits_from_string(parts[0])
        self.maps = []

        for part in parts[1:]:
            part = part.splitlines()
            source, _, destination = part[0].split()[0].split("-")
            maps = []
            for ranges in part[1:]:
                dest_range, source_range, length = extract_digits_from_string(ranges)
                r = Range(
                    source=source,
                    destination=destination,
                    dest_range=dest_range,
                    source_range=source_range,
                    length=length,
                )
                maps.append(r)
            self.maps.append(maps)

    def map(self, value: int, mappings: list[Range]) -> int:
        """Map value, could be seed, or anything else, via mapping"""
        for mapping in mappings:
            if mapping.source_range <= value <= (mapping.source_range + mapping.length):
                # For example,
                # value = 79
                # source_range = 52, length = 48
                # dest_range = 50
                # Expected result: 81
                # eg, difference between dest
                source_list = list(
                    range(
                        mapping.source_range, mapping.source_range + mapping.length + 1
                    )
                )
                dest_list = list(
                    range(mapping.dest_range, mapping.dest_range + mapping.length + 1)
                )
                idx = source_list.index(value)
                value = dest_list[idx]
                return value
        # No mapping found, return as-is
        return value

    def compute_seed(self, seed: int) -> int:
        """Compute the result for seed"""
        # Probably not smart to do it per seed, but cache might help us...
        current_value = seed
        for mapping in self.maps:
            # For each mapping, try to map
            current_value = self.map(current_value, mapping)

        return current_value


class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        results = []
        for seed in tqdm.tqdm(self.seeds):
            print(f"{seed=}")
            value = self.compute_seed(seed)
            results.append(value)

        return min(results)


class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
