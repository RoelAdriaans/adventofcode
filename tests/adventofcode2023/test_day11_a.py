from adventofcodeutils.point import XYNRPoint as Point

from adventofcode2023.day11 import Day11PartA


class TestDay11PartA:
    def test_day11a_parse(self, testdata):
        solution = Day11PartA()
        solution.parse(testdata)
        assert len(solution.galaxy_points) == 9
        assert solution.galaxy_points[0] == Point(0, 3, 0)
        assert solution.galaxy_points[-1] == Point(9, 4, 0)

    def test_day11a_expand(self, testdata):
        solution = Day11PartA()
        solution.parse(testdata)
        solution.expand_universe()
        # No extra galaxies created
        assert len(solution.galaxy_points) == 9
        # First one moved on to the right
        # Check if they are int the list, ordering may have been shuffled
        point_1 = [p for p in solution.galaxy_points if p.nr == 1][0]
        assert point_1.x == 0
        assert point_1.y == 4

        # Find point should be on location (1, 9)
        point_2 = [p for p in solution.galaxy_points if p.nr == 2][0]
        assert point_2.x == 1
        assert point_2.y == 9

        # Find point 9
        point_9 = [p for p in solution.galaxy_points if p.nr == 9][0]
        assert point_9.x == 11
        assert point_9.y == 5

        # After the expansion, the distance between 1 and 7 must be 15
        point_1 = [p for p in solution.galaxy_points if p.nr == 1][0]
        point_7 = [p for p in solution.galaxy_points if p.nr == 7][0]
        assert point_7.distance(point_1) == 15

        # After the expansion, the distance between 3 and 6 must be 17
        point_3 = [p for p in solution.galaxy_points if p.nr == 3][0]
        point_6 = [p for p in solution.galaxy_points if p.nr == 6][0]
        assert point_3.distance(point_6) == 17

        # After the expansion, the distance between 8 and 9 must be 5
        point_8 = [p for p in solution.galaxy_points if p.nr == 8][0]
        point_9 = [p for p in solution.galaxy_points if p.nr == 9][0]
        assert point_8.distance(point_9) == 5

    def test_day11a_testdata(self, testdata):
        solution = Day11PartA()
        result = solution.solve(testdata)
        assert result == 374

    def test_day11a_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res == 9805264
