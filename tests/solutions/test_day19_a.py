import pathlib

from adventofcode2021.solutions.day19 import Day19PartA


class TestDay19PartA:
    def load_testdata(self):
        test_path = (
            pathlib.Path(__file__).parent.parent.parent
            / "src"
            / "adventofcode2021"
            / "solutions"
            / "data"
            / "day_19"
            / "test_data.txt"
        )
        with open(test_path) as f:
            test_data = f.read()
        return test_data

    def test_day19a_solve(self):
        solution = Day19PartA()
        result = solution.solve(self.load_testdata())
        assert result == 79

    def test_day19a_data(self):
        """Result we got when we did the real solution"""
        solution = Day19PartA()
        res = solution("day_19/day19.txt")
        assert res == 323
