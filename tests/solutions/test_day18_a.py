import pytest

from adventofcode2016.solutions.day18 import Day18PartA


class TestDay18PartA:
    def test_simple(self, testdata):
        """Test the short answer"""
        lines = testdata.splitlines()[0]
        solution = Day18PartA()
        for line in lines[1:]:
            result = solution.evolve(lines)
            assert result == line
        assert solution.solve(testdata) == 6



    @pytest.mark.postfix("test2")
    def test_extended(self, testdata):
        """Test the longer answer"""
        lines = testdata.splitlines()[0]
        solution = Day18PartA()

        for line in lines[1:]:
            result = solution.evolve(lines)
            assert result == line

        assert solution.solve(testdata) == 38




    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day18a_solve(self, input_data, expected_result):
        solution = Day18PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day18a_data(self):
        """Result we got when we did the real solution"""
        solution = Day18PartA()
        res = solution("day_18/day18.txt")
        assert res == 0
