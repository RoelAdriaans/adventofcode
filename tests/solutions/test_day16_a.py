import pytest

from adventofcode2020.solutions.day16 import Day16PartA, Ticket


class TestDay16PartA:
    def test_ticket_range(self):
        ticket = Ticket.parse_input("class: 1-3 or 5-7")

        assert ticket.rule == "class"
        assert ticket.is_valid(1)
        assert ticket.is_valid(2)
        assert ticket.is_valid(3)
        assert not ticket.is_valid(4)
        assert ticket.is_valid(5)

    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day16a_solve(self, input_data, expected_result):
        solution = Day16PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 0
