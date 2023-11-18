import pathlib

from adventofcode2021.solutions.day14 import Day14PartB


class TestDay14PartB:
    def load_testdata(self):
        test_path = (
            pathlib.Path(__file__).parent.parent.parent
            / "src"
            / "adventofcode2021"
            / "solutions"
            / "data"
            / "day_14"
            / "test_data.txt"
        )
        with open(test_path) as f:
            test_data = f.read()
        return test_data

    def test_day14a_steps(self):
        solution = Day14PartB()
        solution.initialize(self.load_testdata())

        assert list(solution.cnt.keys()) == ["NN", "NC", "CB"]

        # Do the first step
        solution.step()
        assert list(solution.cnt.keys()) == ["NC", "CN", "NB", "BC", "CH", "HB"]
        solution.step()
        assert list(solution.cnt.keys()) == [
            "NB",
            "BC",
            "CC",
            "CN",
            "BB",
            "CB",
            "BH",
            "HC",
        ]

    def test_day14b_solve(self):
        solution = Day14PartB()
        result = solution.solve(self.load_testdata())
        assert result == 2188189693529

    def test_day14b_data(self):
        """Result we got when we did the real solution"""
        solution = Day14PartB()
        res = solution("day_14/day14.txt")
        assert res == 3015383850689
