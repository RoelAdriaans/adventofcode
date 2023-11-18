import pytest

from adventofcode2016.solutions.day17 import Day17PartA, MazeLocation


class TestDay17PartA:
    @pytest.mark.parametrize(
        ("hash", "open_locations"),
        [
            ("hijkl", "D"),
            ("hijklD", "UR"),
            ("hijklDR", ""),
            ("hijklDU", "R"),
            ("hijklDUR", ""),
        ],
    )
    def test_locations(self, hash, open_locations):
        ml = MazeLocation(0, 0, path=hash)
        open_locations = "".join(direction[2] for direction in ml.get_openlocations())
        assert open_locations == open_locations

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("ihgpwlah", "DDRRRD"),
            ("kglvqrro", "DDUDRLRRUDRD"),
            ("ulqzkmiv", "DRURDRUDDLLDLUURRDULRLDUUDDDRR"),
        ],
    )
    def test_day17a_solve(self, input_data, expected_result):
        result = Day17PartA().run_search(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day17a_data(self):
        """Result we got when we did the real solution"""
        solution = Day17PartA()
        res = solution("day_17/day17.txt")
        assert res == "DDRRUDLRRD"
