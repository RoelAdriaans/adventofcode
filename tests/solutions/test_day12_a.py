import pytest

from adventofcode2021.solutions.day12 import Day12PartA

test_data_short = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

test_data = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

test_data_longer = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


class TestDay12PartA:
    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            (test_data_short, 10),
            (test_data, 19),
            (test_data_longer, 226),
        ],
    )
    def test_day12a_solve(self, input_data, expected_result):
        solution = Day12PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day12a_data(self):
        """Result we got when we did the real solution"""
        solution = Day12PartA()
        res = solution("day_12/day12.txt")
        assert res == 5212
