import pytest
from solutions.day08 import Day08PartB, Node


class TestDay08PartB:
    def test_day08b_nodes(self):
        node_b = Node(metadata=[10, 11, 12])
        assert node_b.value() == 33

        node_d = Node(metadata=[99])
        assert node_d.value() == 99

    def test_day08b_child_nodes(self):
        # Test complex example.
        node_a = Node(metadata=[1, 1, 2])
        node_b = Node(metadata=[10, 11, 12])
        node_c = Node(metadata=[2])
        node_d = Node(metadata=[99])
        node_a.add_child(node_b)
        node_a.add_child(node_c)
        node_c.add_child(node_d)
        # First a simple test:
        assert node_b.value() == 33
        assert node_d.value() == 99

        assert node_c.value() == 0
        assert node_a.value() == 66

    @pytest.mark.parametrize(
        ("input_data", "expected_result"), [("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2", 66)]
    )
    def test_day08b_solve(self, input_data, expected_result):
        solution = Day08PartB()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day08b_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartB()
        res = solution("day_08/day08.txt")
        assert res == 25737
