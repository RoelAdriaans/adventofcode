import pytest

from adventofcode2024.day08 import Day08PartA, Node


class TestDay08PartA:
    def test_day08a_testdata(self, testdata):
        solution = Day08PartA()
        result = solution.solve(testdata)
        assert result == 14

    @pytest.mark.parametrize(
        ("postfix",),
        [("test_1",)],
    )
    def test_day8a_sample(self, testdata_by_postfix):
        solution = Day08PartA()
        # Setting values manually
        solution.max_row = 10
        solution.max_col = 10
        nodes = solution.map_to_nodes(testdata_by_postfix)
        assert len(nodes) == 4
        assert nodes == [
            Node(value="#", row=1, column=3, is_antinode=True),
            Node(value="a", row=3, column=4, is_antinode=False),
            Node(value="a", row=5, column=5, is_antinode=False),
            Node(value="#", row=7, column=6, is_antinode=True),
        ]

        # Finding the antinodes. Before we can do this, we must filter the antinodes from
        # the sample data
        a_nodes = [node for node in nodes if node.value == "a"]
        assert len(a_nodes) == 2

        # Find the antinodes:
        anti_nodes = solution.find_antinodes_in_group(a_nodes)

        assert len(anti_nodes) == 2
        assert anti_nodes == [
            Node(value="#", row=1, column=3, is_antinode=True),
            Node(value="#", row=7, column=6, is_antinode=True),
        ]

    @pytest.mark.parametrize(
        ("postfix", "size", "expected_result"),
        [
            ("test_1", 10, 2),
            ("test_2", 10, 4),
            ("test_3", 11, 14),
        ],
    )
    def test_day8a_multiple_nodes(self, testdata_by_postfix, size, expected_result):
        solution = Day08PartA()
        # Setting values manually
        solution.max_row = size
        solution.max_col = size
        nodes = solution.map_to_nodes(testdata_by_postfix)

        # Finding the antinodes. Before we can do this, we must filter the antinodes from
        # the sample data
        all_nodes = [node for node in nodes if node.value != "#"]
        expected_anti_nodes = [node for node in nodes if node.value == "#"]

        # Find the antinodes:
        anti_nodes = solution.find_antinodes_in_group(all_nodes)

        # Filter out the unique nodes to compare the test input with the created nodes
        # We do this to simplify the comparison when there are multiple same nodes
        unique_anti_nodes = [
            Node(value="#", row=row, column=column, is_antinode=True)
            for row, column in {(node.row, node.column) for node in anti_nodes}
        ]

        assert sorted(unique_anti_nodes) == sorted(expected_anti_nodes)
        assert len(anti_nodes) == expected_result

    def test_day08a_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res > 300
        assert res < 323
        assert res == 0
