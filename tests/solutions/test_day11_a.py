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
        assert facility.elevator == 0
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
        assert facility.list_of_items_from_floor(2) == [("lithium generator",)]
        assert (
            facility.list_of_items_from_floor(0).sort()
            == [
                ("hydrogen microchip",),
                ("lithium microchip",),
                ("hydrogen microchip", "lithium microchip"),
            ].sort()
        )

        sucs = facility.successors()
        # In this case we have only one valid move: Move the Hydrogen microchip to
        # the 2nd floor
        assert len(sucs) == 1
        assert sorted(sucs[0].floors[1]) == sorted(
            [
                "elevator",
                "hydrogen microchip",
                "hydrogen generator",
            ]
        )

    def test_eq_facility(self, testdata):
        facility1 = Day11PartA().parse(testdata)
        facility2 = Day11PartA().parse(testdata)
        assert facility1 == facility2
        assert hash(facility1) == hash(facility2)

    def test_facility_without_elevator(self):
        with pytest.raises(ValueError, match="Elevator not found"):
            FacilityState(floors=[])

    f1 = "The first floor contains a "

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (f1 + "polonium generator, a thulium generator", True),
            (f1 + "polonium generator, a hydrogen-compatible microchip", False),
            (f1 + "polonium generator, a polonium-compatible microchip", True),
            (
                f1 + "polonium generator, a polonium-compatible microchip, "
                "a thulium generator",
                True,
            ),
        ],
    )
    def test_parser_isvalid(self, input_data, expected_result):
        facility = Day11PartA().parse(input_data)
        assert facility.is_legal == expected_result

    def test_parser_solutiondata(self, solutiondata):
        facility = Day11PartA().parse(solutiondata)
        assert facility.is_legal
        assert facility.elevator == 0
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

    def test_day11a_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert res < 113
        assert res != 25
        assert res != 26
        assert res != 27
        assert res == 47
