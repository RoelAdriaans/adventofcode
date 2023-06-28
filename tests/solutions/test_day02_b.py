from adventofcode2016.solutions.day02 import Day02PartB, XYPoint


class TestDay02PartB:
    def test_find_location(self):
        day2 = Day02PartB()
        day2.create_grid()
        assert day2.find_location(1) == XYPoint(0, 2)

        assert day2.find_location(2) == XYPoint(1, 1)
        assert day2.find_location(3) == XYPoint(1, 2)

        assert day2.find_location(5) == XYPoint(2, 0)
        assert day2.find_location(6) == XYPoint(2, 1)
        assert day2.find_location(9) == XYPoint(2, 4)

        assert day2.find_location("A") == XYPoint(3, 1)  # A
        assert day2.find_location("B") == XYPoint(3, 2)  # B
        assert day2.find_location("C") == XYPoint(3, 3)  # C

        assert day2.find_location("D") == XYPoint(4, 2)  # D

    def test_day02b_solve(self, testdata):
        solution = Day02PartB()
        result = solution.solve(testdata)
        assert result == "5DB3"

    def test_day02b_data(self):
        """Result we got when we did the real solution"""
        solution = Day02PartB()
        res = solution("day_02/day02.txt")
        assert res == "CB779"
