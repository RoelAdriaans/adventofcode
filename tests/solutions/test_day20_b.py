import pathlib

from adventofcode2021.solutions.day20 import Day20PartB


class TestDay20PartB:
    @staticmethod
    def load_testdata():
        test_path = (
            pathlib.Path(__file__).parent.parent.parent
            / "src"
            / "adventofcode2021"
            / "solutions"
            / "data"
            / "day_20"
            / "test_data.txt"
        )
        with open(test_path) as f:
            test_data = f.read()
        return test_data

    def test_day20b_solve(self):
        solution = Day20PartB()
        result = solution.solve(self.load_testdata())
        assert result == 3351

    def test_day20b_data(self):
        """Result we got when we did the real solution"""
        solution = Day20PartB()
        res = solution("day_20/day20.txt")
        assert res == 16793
