import pytest

from adventofcode2018.day07 import Day07PartA


class TestDay07PartA:
    test_input = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ]

    def test_parse_string(self):
        solution = Day07PartA()

        assert solution.parse_string(
            "Step C must be finished before step A can begin."
        ) == ("C", "A")

    def test_day07a_get_children(self):
        input_data = "\n".join(self.test_input)
        solution = Day07PartA()
        input_lines = input_data.split("\n")
        nodes = solution.parse_strings(input_lines)
        solution.build_tree(nodes)
        assert solution.get_parent("E") == ["B", "D", "F"]
        assert solution.get_parent("F") == ["C"]
        assert solution.get_parent("C") == []

    def test_day07a_get_root(self):
        input_data = "\n".join(self.test_input)
        solution = Day07PartA()
        input_lines = input_data.split("\n")
        nodes = solution.parse_strings(input_lines)
        solution.build_tree(nodes)
        assert solution.get_root() == "C"

    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [(test_input, "CABDFE")]
    )
    def test_day07a_solve(self, input_data, expected_result):
        input_data = "\n".join(input_data)
        solution = Day07PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day07a_data(self):
        """Result we got when we did the real solution"""
        solution = Day07PartA()
        res = solution("day_07/day07.txt")
        assert res != "SEFDGJLPKNRYOAMQIUHTCVWZXB"
        assert res[0] != "C"
        assert res == "FDSEGJLPKNRYOAMQIUHTCVWZXB"
