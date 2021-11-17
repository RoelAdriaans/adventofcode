from adventofcode2020.solutions.day16 import Day16PartB


class TestDay16PartB:
    def test_day16b_solve(self):
        test_data = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
1,99,9
"""
        solution = Day16PartB()
        solution.parse(test_data)

        assert len(solution.nearby_tickets) == 4
        solution.remove_invalid_tickets()
        assert len(solution.nearby_tickets) == 3

        mapping = solution.compute_mapping()

        assert mapping["class"] == 1
        assert mapping["row"] == 0
        assert mapping["seat"] == 2

        assert solution.my_tickets[mapping["class"]] == 12
        assert solution.my_tickets[mapping["row"]] == 11
        assert solution.my_tickets[mapping["seat"]] == 13

    def test_day16b_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartB()
        res = solution("day_16/day16.txt")
        assert res == 4810284647569
