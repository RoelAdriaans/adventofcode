import pathlib

from adventofcode2021.solutions.day19 import Day19PartB


class TestDay19PartB:
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

    def test_day19b_solve(self):
        solution = Day19PartB()
        result = solution.solve(self.load_testdata())
        assert result == 3621

    def test_day19b_data(self):
        """Result we got when we did the real solution"""
        solution = Day19PartB()
        res = solution("day_19/day19.txt")
        assert res == 10685
