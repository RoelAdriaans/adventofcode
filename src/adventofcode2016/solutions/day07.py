from __future__ import annotations

import itertools
import re

import attrs

from adventofcode2016.utils.abstract import FileReaderSolution


@attrs.define
class IPv7:
    address: str
    hypernets: list[str]
    address_parts: list[str]

    @classmethod
    def from_string(cls, string) -> IPv7:
        address = string
        # Find all the parts inside the square brackets
        hypernets = re.findall(r"\[(.*?)]", string)

        # All parts outside the hypernets
        address_parts = re.sub(r"\[(.*?)]", " ", string).split(" ")

        return cls(address=address, hypernets=hypernets, address_parts=address_parts)

    @staticmethod
    def has_abba(text: str) -> bool:
        """Is this piece of code a dancing queen?"""

        for n in range(len(text) - 3):
            begin = text[n : n + 2]
            end = text[n + 3 : n + 1 : -1]
            # if not len(set(begin + end)) == 2:
            if begin == end and len(set(begin + end)) == 2:
                return True

        return False

    @staticmethod
    def has_aba(text: str) -> list[str]:
        """Return all the aba matches in a string"""
        results = []
        for n in range(len(text) - 2):
            if text[n] == text[n + 2] and text[n] != text[n + 1]:
                results.append(text[n : n + 3])
        return results

    @staticmethod
    def is_inverse(a, b) -> bool:
        """Check if a is the inverse of b.
        eg: is_inverse("zaz", "aza") == True
        eg: is_inverse("zaz", "boz") == False

        Only supports 3 character strings
        """
        if a == b:
            return False

        return (
            a[0] == b[1]
            and a[1] == b[0]
            and a[1] == b[2]
            and a[0] == a[2]
            and b[0] == b[2]
            and b[1] == a[0]
        )

    @property
    def supports_tls(self) -> bool:
        """Test if IPv7 address supports tls (transport-layer snooping)"""
        # First, check if any of the chars parts have abba. At least one needs this
        address_parts_abba = any(self.has_abba(part) for part in self.address_parts)
        # Condition for the hypernet
        hypernet_parts_abba = any(self.has_abba(part) for part in self.hypernets)

        # front OR back must have abba, and hypernet should NOT have abba
        return address_parts_abba and not hypernet_parts_abba

    @property
    def supports_ssl(self) -> bool:
        """Test if IPv7 address supports SSL (super-secret listening)."""
        # First, check if any of the chars parts have abba. At least one needs this
        address_parts_aba = list(
            itertools.chain.from_iterable(
                self.has_aba(text) for text in self.address_parts
            )
        )
        hypernet_parts_aba = list(
            itertools.chain.from_iterable(self.has_aba(text) for text in self.hypernets)
        )
        matches = itertools.product(address_parts_aba, hypernet_parts_aba)
        return any(IPv7.is_inverse(a, b) for a, b in matches)


class Day07:
    pass


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(
            IPv7.from_string(address).supports_tls
            for address in input_data.splitlines()
        )


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return sum(
            IPv7.from_string(address).supports_ssl
            for address in input_data.splitlines()
        )
