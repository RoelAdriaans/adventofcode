import textwrap

import pytest

from adventofcode2016.solutions.day11 import Day11PartA, FacilityState


class TestDay11PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("elevator", "E "),
            ("polonium generator", "PG"),
            ("thulium-compatible microchip", "TM"),
        ],
    )
    def test_str_element(self, input_data, expected_result):
        assert FacilityState.str_element(input_data) == expected_result

    def test_parser(self, testdata):
        facility = Day11PartA().parse(testdata)
        assert facility.is_legal
        assert len(facility.floors) == 4
        assert facility.floors[0] == [
            "elevator",
            "hydrogen microchip",
            "lithium microchip",
        ]
        assert str(facility) == "\n".join(
            [
                "F4",
                "F3 LIGE",
                "F2 HYGE",
                "F1 ELEV HYMI LIMI",
            ]
        )

    f1 = "The first floor contains a "

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (f1 + "polonium generator, a thulium generator", True),
            (f1 + "polonium generator, a hydrogen-compatible microchip", False),
            (f1 + "polonium generator, a polonium-compatible microchip", True),
        ],
    )
    def test_parser_isvalid(self, input_data, expected_result):
        facility = Day11PartA().parse(input_data)
        assert facility.is_legal == expected_result

    def test_parser_solutiondata(self, solutiondata):
        facility = Day11PartA().parse(solutiondata)
        assert facility.is_legal
        assert len(facility.floors) == 4
        assert facility.floors[0] == [
            "elevator",
            "polonium generator",
            "thulium generator",
            "thulium microchip",
            "promethium generator",
            "ruthenium generator",
            "ruthenium microchip",
            "cobalt generator",
            "cobalt microchip",
        ]
        assert facility.floors[1] == ["polonium microchip", "promethium microchip"]
        assert str(facility) == "\n".join(
            [
                "F4",
                "F3",
                "F2 POMI PRMI",
                "F1 ELEV POGE THGE THMI PRGE RUGE RUMI COGE COMI",
            ]
        )

    def test_day11a_solve(self, testdata):
        solution = Day11PartA()
        result = solution.solve(testdata)
        assert result == 11

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day11a_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res == 0
