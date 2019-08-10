import pytest

from solutions.day07 import Day07PartB, TimedNode


class TestDay07PartB:
    def test_day07b_timed_node(self):
        node = TimedNode("C", extra_seconds=5)
        assert node.seconds_worked_on == 0
        # Seconds left == 3 + 5
        # A=1, B=2, C=3
        assert node.seconds_to_work == 8
        assert node.time_left() == 8

        node = TimedNode("C", extra_seconds=0)
        assert node.is_complete() is False
        assert node.time_left() == 3

        node.work()
        assert node.is_complete() is False
        assert node.time_left() == 2

        node.work()
        assert node.is_complete() is False
        assert node.time_left() == 1

        node.work()
        assert node.is_complete() is True
        assert node.time_left() == 0
        assert repr(node) == "C (3 - 3)"

        # When we work more, keep time left at 0
        node.work()
        assert node.is_complete() is True
        assert node.time_left() == 0

        # also test the real input;
        node = TimedNode("Z", extra_seconds=60)
        assert node.seconds_worked_on == 0
        assert node.seconds_to_work == 86
        assert node.time_left() == 86
        assert repr(node) == "Z (86 - 0)"

    test_input = [
        "Step C must be finished before step A can begin.",
        "Step C must be finished before step F can begin.",
        "Step A must be finished before step B can begin.",
        "Step A must be finished before step D can begin.",
        "Step B must be finished before step E can begin.",
        "Step D must be finished before step E can begin.",
        "Step F must be finished before step E can begin.",
    ]

    @pytest.mark.parametrize(("input_data", "expected_result"), [(test_input, 15)])
    def test_day07b_solve(self, input_data, expected_result):
        solution = Day07PartB()
        input_data = "\n".join(self.test_input)
        result = solution.solve(input_data, extra_time=0, num_workers=2)
        assert result == expected_result

    def test_day07b_data(self):
        """ Result we got when we did the real solution """
        solution = Day07PartB()
        res = solution("day_07/day07.txt")
        assert res != 1002
        assert res == 1000
