import re
from typing import List, NamedTuple

from adventofcode2020.utils.abstract import FileReaderSolution


class Ticket(NamedTuple):
    rule: str
    upper_range_1: int
    lower_range_1: int
    upper_range_2: int
    lower_range_2: int

    @staticmethod
    def parse_input(rule: str) -> "Ticket":
        """
        Parse input, for example:
        departure track: 37-608 or 623-964
        """
        regex = r"^(.*): (\d*)-(\d*) or (\d*)-(\d*)"
        results = re.match(regex, rule)

        return Ticket(
            rule=results[1],
            lower_range_1=int(results[2]),
            upper_range_1=int(results[3]),
            lower_range_2=int(results[4]),
            upper_range_2=int(results[5]),
        )

    def is_valid(self, number) -> bool:
        """Is this number valid?"""
        if (
            self.lower_range_1 <= number <= self.upper_range_1
            or self.lower_range_2 <= number <= self.upper_range_2
        ):
            return True
        else:
            return False


class Day16:
    ticket_rules: List[Ticket]
    my_tickets: List[int]
    nearby_tickets: List[List[int]]

    def parse(self, input_data):
        rules, my_tickets, nearby = input_data.split("\n\n")
        self.ticket_rules = [
            Ticket.parse_input(rule) for rule in rules.split("\n") if rule
        ]
        self.my_tickets = [
            int(ticket) for ticket in my_tickets.split("\n")[1].split(",")
        ]

        rows = [row.split(",") for row in nearby.split("\n")[1:] if row]

        self.nearby_tickets = []
        for row in rows:
            self.nearby_tickets.append([int(x) for x in row])


class Day16PartA(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        numbers = [val for sublist in self.nearby_tickets for val in sublist]
        error = []
        for number in numbers:
            valids = [rule.is_valid(number) for rule in self.ticket_rules]
            if not any(valids):
                error.append(number)

        return sum(error)


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
