import pytest

from adventofcode2020.day16 import Day16PartA, Ticket


class TestDay16PartA:
    def test_invalid_ticket(self):
        with pytest.raises(ValueError):
            Ticket.parse_input("class 1-3, 5-7")

    def test_ticket_range(self):
        ticket = Ticket.parse_input("class: 1-3 or 5-7")

        assert ticket.rule == "class"
        assert ticket.is_valid(1)
        assert ticket.is_valid(2)
        assert ticket.is_valid(3)
        assert not ticket.is_valid(4)
        assert ticket.is_valid(5)

    def test_day16a_solve(self):
        test_data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""
        solution = Day16PartA()
        result = solution.solve(test_data)
        assert result == 71

    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 20048
