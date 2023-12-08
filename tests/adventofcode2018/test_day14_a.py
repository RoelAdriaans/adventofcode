import pytest

from adventofcode2018.day14 import Day14PartA


class TestDay14PartA:
    def test_day14a_test_input(self):
        input_data = "37"
        solution = Day14PartA()
        solution.parse_data(input_data)
        assert len(solution.scoreboard) == 2

    def test_day14a_test_compute_digits(self):
        # Test for one digit
        input_data = "23"
        solution = Day14PartA()
        solution.initalise(input_data, num_elves=2)
        assert solution.compute_new_recipes() == [5]

    def test_day14a_test_compute(self):
        input_data = "37"
        solution = Day14PartA()
        solution.initalise(input_data, num_elves=2)
        assert len(solution.elves) == 2
        assert solution.elves[0].current_recipe == 3
        assert solution.elves[1].current_recipe == 7
        assert solution.elves[0].current_recipe_idx == 0
        assert solution.elves[1].current_recipe_idx == 1

        assert solution.compute_new_recipes() == [1, 0]

        solution.compute_next_recipes(num_recipes=1)
        # After the first round the elves should be at the same position
        assert len(solution.scoreboard) == 4
        assert solution.scoreboard == [3, 7, 1, 0]
        assert solution.elves[0].current_recipe == 3
        assert solution.elves[1].current_recipe == 7
        assert solution.elves[0].current_recipe_idx == 0
        assert solution.elves[1].current_recipe_idx == 1

        # Next step
        solution.compute_next_recipes(num_recipes=1)
        assert len(solution.scoreboard) == 6
        assert solution.scoreboard == [3, 7, 1, 0, 1, 0]
        assert solution.elves[0].current_recipe_idx == 4
        assert solution.elves[1].current_recipe_idx == 3

        # Let's go to the lest step
        solution.compute_next_recipes(num_recipes=13)
        round_15 = [3, 7, 1, 0, 1, 0, 1, 2, 4, 5, 1, 5, 8, 9, 1, 6, 7, 7, 9, 2]
        assert solution.scoreboard == round_15

    def test_day14a_test_num_recipes_created(self):
        input_data = "37"
        solution = Day14PartA()
        solution.initalise(input_data, num_elves=2)
        solution.compute_recipe_length(num_recipes_created=19)
        assert len(solution.scoreboard) == 19

    @pytest.mark.parametrize(
        ("input_data", "after_num_recipes", "expected_result"),
        [
            ("37", 9, "5158916779"),
            ("37", 5, "0124515891"),
            ("37", 18, "9251071085"),
            ("37", 2018, "5941429882"),
        ],
    )
    def test_day14a_solve(self, input_data, after_num_recipes, expected_result):
        solution = Day14PartA()
        solution.initalise(input_data=input_data, num_elves=2)

        num_recipes_needed = after_num_recipes + 10
        solution.compute_recipe_length(num_recipes_created=num_recipes_needed)
        # We need at least this many recipes. It can be more, last step could have
        # double digits
        assert len(solution.scoreboard) >= num_recipes_needed

        result = solution.total_score(after_num_recipes)
        assert result == expected_result

    def test_day14a_data(self):
        """Result we got when we did the real solution"""
        solution = Day14PartA()
        res = solution("day_14/day14.txt")
        assert res != "4281681601"
        assert res == "1342316410"
