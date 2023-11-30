import pytest

from adventofcode2022.day17 import Day17PartA, Tile


class TestDay17PartA:
    @pytest.mark.parametrize(
        ("input_line", "idx", "expected_result"),
        [
            ("..@@@@.", 1, "...@@@@"),
            ("...@@@@", 1, "...@@@@"),
            ("..@@@@#", 1, "..@@@@#"),  # Cannot move to the right anymore
            ("#...@.#", 1, "#....@#"),  # Move one to the right, keep empty
            ("#....@#", 1, "#...@.#"),  # Move one to the left, keep empty
        ],
    )
    def test_move_line(self, input_line, idx, expected_result):
        # First build the line
        mapping = str.maketrans(".@#", "012")
        input_tiles = [Tile(int(char)) for char in input_line.translate(mapping)]
        expected_output_tiles = [
            Tile(int(char)) for char in expected_result.translate(mapping)
        ]

        output = Day17PartA.move_line(idx, input_tiles)
        assert output == expected_output_tiles

    def test_day17a_testdata(self, testdata):
        solution = Day17PartA()
        result = solution.solve(testdata)
        assert result == 3068

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day17a_data(self):
        """Result we got when we did the real solution"""
        solution = Day17PartA()
        res = solution("day_17/day17.txt")
        assert res == 0
