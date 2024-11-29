from textwrap import dedent

import pytest

from adventofcode2021.day18 import Day18PartB


class TestDay18PartB:
    def test_day18b_solve(self):
        test_data = """\
        [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
        [[[5,[2,8]],4],[5,[[9,9],0]]]
        [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
        [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
        [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
        [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
        [[[[5,4],[7,7]],8],[[8,3],8]]
        [[9,3],[[9,9],[6,[4,9]]]]
        [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
        [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
        """
        solution = Day18PartB()
        result = solution.solve(dedent(test_data))
        assert result == 3993

    @pytest.mark.slow
    def test_day18b_data(self):
        """Result we got when we did the real solution"""
        solution = Day18PartB()
        res = solution("day_18/day18.txt")
        assert res == 4616
