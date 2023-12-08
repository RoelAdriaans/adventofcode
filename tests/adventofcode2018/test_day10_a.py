import pytest
from solutions.day10 import Day10PartA, Point


class TestDay10PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("position=< 9,  1> velocity=< 0,  2>", [9, 1, 0, 2]),
            ("position=< 3, -2> velocity=<-1,  1>", [3, -2, -1, 1]),
            ("position=<15,  0> velocity=<-2,  0>", [15, 0, -2, 0]),
            ("position=<-31716, -42432> velocity=< 3,  4>", [-31716, -42432, 3, 4]),
        ],
    )
    def test_day10a_test_string(self, input_data, expected_result):
        result = Day10PartA().parse_string(input_data)
        point = Point(*expected_result)
        assert result == point
        assert "position" in result.__repr__()

    @pytest.mark.parametrize(
        ("input_data", "seconds", "expected_result"),
        [("position=< 3,  9> velocity=< 1,  -2>", 3, [6, 3])],
    )
    def test_day10a_test_compute(self, input_data, seconds, expected_result):
        result = Day10PartA().parse_string(input_data)
        for x in range(0, seconds):
            result.compute_step(seconds=1)

        point_seconds = Day10PartA().parse_string(input_data)
        point_seconds.compute_step(seconds=seconds)

        expected_point = Point(
            x=expected_result[0],
            y=expected_result[1],
            vel_x=result.vel_x,
            vel_y=result.vel_y,
        )
        assert point_seconds == expected_point
        assert result == expected_point

    def test_day10a_testdata(self):
        """Run with test data"""
        solution = Day10PartA()
        res = solution("day_10/day10_test.txt")
        assert res == 3

    def test_day10a_data(self):
        """Result we got when we did the real solution"""
        solution = Day10PartA()
        res = solution("day_10/day10.txt")
        # We cannot do a real test, but we can compute the iteration that should
        # have our image.
        assert res == 10645
