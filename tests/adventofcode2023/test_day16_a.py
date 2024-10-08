from adventofcode2023.day16 import Day16PartA, Beam, XYPoint, Direction


class TestDay16PartA:

    def test_beam_eq_direction(self):
        """Test that a beam in the single location is equal is direction matches."""
        beam_right = Beam(XYPoint(1, 2), Direction.RIGHT)
        beam_left = Beam(XYPoint(1, 2), Direction.LEFT)
        beam_up = Beam(XYPoint(1, 2), Direction.UP)
        beam_down = Beam(XYPoint(1, 2), Direction.DOWN)

        assert beam_right == beam_right

        assert beam_right == beam_left
        assert beam_up == beam_down

        assert beam_right != beam_down
        assert beam_left != beam_down

    def test_beam_eq_location(self):
        """Test beam locations equalise."""
        beam_1 = Beam(XYPoint(1, 2), Direction.RIGHT)
        beam_2 = Beam(XYPoint(2, 2), Direction.RIGHT)

        assert beam_1 == beam_1
        assert beam_1 != beam_2

    def test_beam_in_set(self):
        """Validate that hashing on the Beam does take orientation correctly."""
        beamset = {
            Beam(XYPoint(2, 2), Direction.RIGHT),
            Beam(XYPoint(4, 3), Direction.DOWN),
        }

        assert Beam(XYPoint(2, 2), Direction.RIGHT) in beamset
        assert Beam(XYPoint(2, 2), Direction.LEFT) in beamset
        assert Beam(XYPoint(2, 2), Direction.UP) not in beamset
        assert Beam(XYPoint(2, 2), Direction.DOWN) not in beamset

        assert Beam(XYPoint(4, 3), Direction.DOWN) in beamset
        assert Beam(XYPoint(4, 3), Direction.UP) in beamset
        assert Beam(XYPoint(4, 3), Direction.LEFT) not in beamset

    def test_day16a_testdata(self, testdata):
        solution = Day16PartA()
        result = solution.solve(testdata)
        assert result == 46


    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 0
