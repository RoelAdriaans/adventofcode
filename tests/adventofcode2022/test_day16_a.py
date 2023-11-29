from adventofcode2022.day16 import Day16PartA


class TestDay16PartA:
    def test_day16a_parsing(self, testdata):
        solution = Day16PartA()
        solution.parse(testdata)
        assert len(solution.valves) == 10
        assert solution.valves["AA"].flow_rate == 0

        assert solution.valves["JJ"].flow_rate == 21
        assert solution.valves["DD"].connections == ("CC", "AA", "EE")
        # Make sure the Valve is hashable
        assert hash(solution.valves["DD"])

    def test_day16a_testdata(self, testdata):
        solution = Day16PartA()
        result = solution.solve(testdata)
        assert result == 1651

    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 1767
