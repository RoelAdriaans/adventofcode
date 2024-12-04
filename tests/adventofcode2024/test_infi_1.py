import pytest

from adventofcode2024.infi import InfiPart1


class TestInfiPart1:
    def test_infi1_testdata(self):
        # Because we're not dealing with a standard AOC path, we have to read the
        # file by hand
        with open("testdata/infi/infi_test.txt") as f:
            testdata = f.read()
        solution = InfiPart1()
        result = solution.solve(testdata)
        assert result == 5686200

    def test_for_instruction(self):
        with open("testdata/infi/infi_test.txt") as f:
            testdata = f.read()
        solution = InfiPart1()
        result = solution.solve_for_location(testdata.splitlines(), 7, 0, 0)
        assert result == 123

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day05a_data(self):
        """Result we got when we did the real solution"""
        solution = InfiPart1()
        res = solution("infi/infi.txt")
        assert res == 4633
