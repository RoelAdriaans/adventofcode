from __future__ import annotations

import itertools
from functools import cache

import attrs
from adventofcodeutils.parsing import extract_digits_from_string
from functools import cache
from adventofcode.utils.abstract import FileReaderSolution
import itertools


@attrs.define(frozen=True)
class Range:
    source: str
    destination: str

    dest_range: int
    source_range: int
    length: int


class Day05:
    seeds: list[int]
    maps: list[tuple[Range]]

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
            self.maps.append(tuple(maps))

    @cache
    def map(self, value: int, mappings: tuple[Range]) -> int:
        """Map value, could be seed, or anything else, via mapping"""
        for mapping in mappings:
            if mapping.source_range <= value <= (mapping.source_range + mapping.length):
                delta = mapping.dest_range - mapping.source_range
                value = value + delta
                return value
        # No mapping found, return as-is
        return value

    @cache
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
        for seed in self.seeds:
            value = self.compute_seed(seed)
            results.append(value)

        return min(results)


class Day05PartB(Day05, FileReaderSolution):
    def reverse_map(self, location: int, mapping) -> int:
        return location - 2

    def reverse_location_valid(self, location) -> bool:
        """Test if the seed is valid"""
        current_location = location
        for mapping in reversed(self.maps):
            current_location = self.reverse_map(current_location, mapping)

        return False

    def seed_in_seeds(self, seed: int) -> bool:
        """Is seed in seed pairs"""
        return False

    def reverse_search(self) -> int:
        # First, get the seeds
        seed_pairs = sorted(itertools.batched(self.seeds, n=2))
        # Find out the maximum seed, probably? I hope we find a location before this
        max_seed = seed_pairs[-1][0] + seed_pairs[-1][1]
        for location in range(max_seed):
            if seed := self.reverse_location_valid(location):
                if self.seed_in_seeds(seed):
                    return location
        raise ValueError("No valid locations found")

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        # Reverse Search!
        return self.reverse_search()
