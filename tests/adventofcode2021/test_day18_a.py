from textwrap import dedent

import pytest

from adventofcode2021.solutions.day18 import Day18PartA, Snail


class TestDay18PartA:
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

    def test_repr(self):
        zero_snail = Snail(value=0)
        assert repr(zero_snail) == "0"

    def test_single_snail(self):
        test_snail = "[3,9]"
        root_snail = Day18PartA().create_tree(test_snail)
        assert root_snail.left.value == 3
        assert root_snail.right.value == 9
        assert repr(root_snail) == test_snail

        # Not deep enough for an explosion to happen
        deepest, depth = root_snail.find_deepest_snail()
        assert deepest is None
        assert depth == 0

    def test_simple_parsing(self):
        """Simple example"""
        test_snail = "[1,[2,3]]"
        root_snail = Day18PartA().create_tree(test_snail)
        assert root_snail.left.value == 1
        assert root_snail.right.left.value == 2
        assert root_snail.right.right.value == 3
        assert root_snail.right.parent is root_snail
        assert repr(root_snail) == test_snail

        # Not deep enough for an explosion to happen
        deepest, depth = root_snail.find_deepest_snail()
        assert deepest is None
        assert depth == 0

    def test_complex_parsing(self):
        """Now, make is what more complex"""
        test_snail = "[[[[[9,8],1],2],3],4]"
        root_snail = Day18PartA().create_tree(test_snail)
        assert root_snail.right.value == 4
        # [[[[9,8],1],2],3]
        assert root_snail.left.right.value == 3
        # [[[9,8],1],2]
        assert root_snail.left.left.right.value == 2
        assert root_snail.left.parent is root_snail
        assert root_snail.left.left.left.parent is root_snail.left.left
        assert repr(root_snail) == test_snail
        deepest, depth = Snail.find_deepest_snail(root_snail)
        assert repr(deepest) == "[9,8]"
        assert depth == 5

    def test_addition(self):
        snail1 = Day18PartA().create_tree("[1,2]")
        snail2 = Day18PartA().create_tree("[[3,4],5]")

        combined = snail1 + snail2
        assert repr(combined) == "[[1,2],[[3,4],5]]"

    def test_deepest(self):
        snail = Day18PartA().create_tree("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
        deepest, depth = snail.find_deepest_snail()
        assert repr(deepest) == "[4,3]"
        assert depth == 5

    def test_full_example(self):
        snail1_str = "[[[[4,3],4],4],[7,[[8,4],9]]]"
        snail2_str = "[1,1]"

        snail1 = Day18PartA().create_tree(snail1_str)
        assert repr(snail1) == snail1_str

        snail2 = Day18PartA().create_tree(snail2_str)
        assert repr(snail2) == snail2_str

        snail = snail1 + snail2
        assert repr(snail) == "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"

        # Time to explode, first time
        snail = Day18PartA().explode(snail)
        assert repr(snail) == "[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"

        # Time to explode, second time
        snail = Day18PartA().explode(snail)
        assert repr(snail) == "[[[[0,7],4],[15,[0,13]]],[1,1]]"

        # We cannot explode anymore:
        deepest, depth = snail.find_deepest_snail()
        assert deepest is None
        assert depth == 0

        # And also the explode function will not change anything
        with pytest.raises(StopIteration):
            Day18PartA().explode(snail)
        assert repr(snail) == "[[[[0,7],4],[15,[0,13]]],[1,1]]"

        # Time to split:
        snail = Day18PartA().split(snail)
        assert repr(snail) == "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"
        snail = Day18PartA().split(snail)
        assert repr(snail) == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
        # And a new split does nothing:
        with pytest.raises(StopIteration):
            Day18PartA().split(snail)
        assert repr(snail) == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"

        # Explode for the last time:
        final_state = "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

        snail = Day18PartA().explode(snail)
        assert repr(snail) == final_state

        # Exploding of splitting will no longer update the state
        with pytest.raises(StopIteration):
            Day18PartA().explode(snail)
        assert repr(snail) == final_state
        with pytest.raises(StopIteration):
            Day18PartA().split(snail)
        assert repr(snail) == final_state

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
            ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
            ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
            (
                "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]",
                "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]",
            ),
        ],
    )
    def test_explode(self, input_data, expected_result):
        solution = Day18PartA()
        root_node = solution.create_tree(input_data)
        exploded = solution.explode(root_node)
        assert repr(exploded) == expected_result

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("[[[[0,7],4],[15,[0,13]]],[1,1]]", "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]"),
            (
                "[[[[0,7],4],[[7,8],[0,13]]],[1,1]]",
                "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]",
            ),
        ],
    )
    def test_split(self, input_data, expected_result):
        solution = Day18PartA()
        root_node = solution.create_tree(input_data)
        splitted = solution.split(root_node)
        assert repr(splitted) == expected_result

    def test_reduce(self):
        solution = Day18PartA()
        snail1 = solution.create_tree("[[[[4,3],4],4],[7,[[8,4],9]]]")
        snail2 = solution.create_tree("[1,1]")

        result = solution.reduce(snail1, snail2)
        assert repr(result) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("[9,1]", 29),
            ("[1,9]", 21),
            ("[[9,1],[1,9]]", 129),
            ("[[1,2],[[3,4],5]]", 143),
            ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
            ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
            ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
            ("[[[[5,0],[7,4]],[5,5]],[6,6]]", 1137),
            ("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", 3488),
        ],
    )
    def test_magnitude(self, input_data, expected_result):
        solution = Day18PartA()
        snail = solution.create_tree(input_data)
        assert solution.magnitude(snail) == expected_result

    def test_day18a_solve(self):
        solution = Day18PartA()
        result = solution.solve(dedent(self.test_data))
        assert result == 4140

    def test_day18a_data(self):
        """Result we got when we did the real solution"""
        solution = Day18PartA()
        res = solution("day_18/day18.txt")
        assert res == 3359
