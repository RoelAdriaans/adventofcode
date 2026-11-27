from itertools import combinations

import pytest

from adventofcode2025.day08 import Day08PartA, Junction


class TestDay08PartA:
    def test_parse_testdata(self, testdata):
        boxes = Day08PartA.create_junction_boxes(testdata)
        assert len(boxes) == len(testdata.splitlines())
        assert boxes[0] == Junction(162, 817, 812)
        assert boxes[-1] == Junction(425, 690, 689)

    def test_distance(self):
        j1 = Junction(162, 817, 812)
        j2 = Junction(425, 690, 689)
        assert j1.distance(j1) == 0
        # Reversible
        assert j1.distance(j2) == j2.distance(j1)

        assert round(j1.distance(j2), 3) == 316.902

    def test_closest_together(self, testdata):
        # Find the closest once together. This should be in the solution, but for now
        # in tests to check distance function
        boxes = Day08PartA.create_junction_boxes(testdata)
        pairs = []
        for box1, box2 in combinations(boxes, 2):
            distance = box1.distance(box2)
            pairs.append((box1, box2, distance))

        # pairs.sort(key=lambda x: x[2])
        assert pairs[0][0] == Junction(162, 817, 812)
        assert pairs[0][1] == Junction(425, 690, 689)
        assert round(pairs[0][2], 3) == 316.902

    def test_day08a_testdata(self, testdata):
        solution = Day08PartA()
        result = solution.solve(testdata)
        assert result == 40

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day08a_solve(self, input_data, expected_result):
        solution = Day08PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day08a_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartA()
        res = solution("day_08/day08.txt")
        assert res == 0
