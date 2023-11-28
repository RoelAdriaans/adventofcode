from adventofcode2021.day14 import Day14PartA


class TestDay14PartA:
    def test_day14a_steps(self, testdata):
        solution = Day14PartA()
        solution.initialize(testdata)

        assert "".join(solution.polimers_to_list()) == "NNCB"

        # Do the first step
        solution.step()
        assert "".join(solution.polimers_to_list()) == "NCNBCHB"
        solution.step()
        assert "".join(solution.polimers_to_list()) == "NBCCNBBBCBHCB"
        solution.step()
        assert "".join(solution.polimers_to_list()) == "NBBBCNCCNBBNBNBBCHBHHBCHB"
        solution.step()
        assert (
            "".join(solution.polimers_to_list())
            == "NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB"
        )

    def test_day14a_solve(self, testdata):
        solution = Day14PartA()
        result = solution.solve(testdata)
        assert result == 1588

    def test_day14a_data(self):
        """Result we got when we did the real solution"""
        solution = Day14PartA()
        res = solution("day_14/day14.txt")
        assert res != 3292
        assert res == 2975
