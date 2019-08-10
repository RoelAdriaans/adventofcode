import pytest

from solutions.day08 import Day08PartA


class TestDay08PartA:
    def test_day08_test_str_to_ints(self):
        input_data = "2 3 392 42 191 302 192"
        solution = Day08PartA()
        result = solution.parse_data(input_data)
        assert result == [2, 3, 392, 42, 191, 302, 192]

    def test_day08_build_tree(self):
        input_data = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        solution = Day08PartA()
        list_ints = solution.parse_data(input_data)
        result = solution.create_nodes(list_ints)
        # Check that we have created 4 nodes?
        assert len(solution.nodes) == 4

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2", 138)],
    )
    def test_day08a_solve(self, input_data, expected_result):
        solution = Day08PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day08a_data(self):
        """ Result we got when we did the real solution """
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 41760
