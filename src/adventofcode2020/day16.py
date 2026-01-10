import math
import re
from typing import NamedTuple

from adventofcode.utils.abstract import FileReaderSolution


class Ticket(NamedTuple):
    rule: str
    upper_range_1: int
    lower_range_1: int
    upper_range_2: int
    lower_range_2: int

    @staticmethod
    def parse_input(rule: str) -> Ticket:
        """
        Parse input, for example:
        departure track: 37-608 or 623-964
        """
        regex = r"^(.*): (\d*)-(\d*) or (\d*)-(\d*)"
        results = re.match(regex, rule)

        if not results:
            raise ValueError("Rule is not valid")

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
    ticket_rules: list[Ticket]
    my_tickets: list[int]
    nearby_tickets: list[list[int]]

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
    def remove_invalid_tickets(self):
        """Remove the invalid tickets from self.nearby_tickets"""
        valid_tickets = []
        for ticket in self.nearby_tickets:
            valids = []
            for number in ticket:
                valids.append(
                    any([rule.is_valid(number) for rule in self.ticket_rules])
                )
            if all(valids):
                valid_tickets.append(ticket)
        self.nearby_tickets = valid_tickets

    def compute_mapping(self) -> dict[str, int]:
        """Compute the mapping from all the valid tickets

        We need to find the rules that we can apply here. Algorirm:
        Create a dict aith all the options, and all the rows, eg:
        class: 0, 1, 2
        row:  0, 1, 2
        seat:  0, 1, 2

        Now we need to figure out from the right options.
        So, for every ticket we seek the options:
        Ticket 1: 3, 9, 18
        3 -> Valid for row and seat. Delete 0 from class, no match
        9 and 18 -> Valid for row, seat and class. Do nothing.

        In the end we should end up with only one option per group.
        """

        options: dict[str, set[int]] = {}

        for rule in self.ticket_rules:
            options[rule.rule] = set(range(len(self.my_tickets)))

        for ticket in self.nearby_tickets:
            for idx, number in enumerate(ticket):
                # idx will have the option index, number will have the ticket number
                for rule in self.ticket_rules:
                    if not rule.is_valid(number):
                        options[rule.rule].discard(idx)

        # We now have eliminated all the options, but we have to remove the duplicates
        # Eg in out test data:
        # seat: 2
        # class: 1, 2
        # row: 0, 1, 2
        # This ends up as seat 2, class 1, row = 0
        # Loop for as long we have an set that is bigger then one
        while any([len(s) > 1 for s in options.values()]):
            for ticket_rule in options:
                if len(options[ticket_rule]) == 1:
                    # We have only option, remove this option from the rest of the set
                    for remove in options:
                        if remove != ticket_rule:
                            options[remove].discard(list(options[ticket_rule])[0])

        # Cleanup, remove set
        cleaned_options: dict[str, int] = {}
        for cleanup_rule in options:
            cleaned_options[cleanup_rule] = list(options[cleanup_rule])[0]

        return cleaned_options

    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        self.remove_invalid_tickets()
        mapping = self.compute_mapping()

        numbers = []
        for rule in self.ticket_rules:
            if "departure" in rule.rule:
                index = mapping[rule.rule]
                numbers.append(self.my_tickets[index])

        # Compute the product
        product = math.prod(numbers)
        return product
