from solutions.day13 import Day13PartB


class TestDay13PartB:
    def test_day13b_simple(self):
        # Create the grid from the example:
        # />-<\
        # |   |
        # | /<+-\
        # | | | v
        # \>+</ |
        #   |   ^
        #   \<->/

        solution = Day13PartB()

        solution.build_grid(
            [
                "/>-<\\  ",
                "|   |   ",
                "| /<+-\\",
                "| | | v ",
                "\\>+</ |",
                "  |   ^ ",
                "  \\<->/",
            ]
        )
        assert len(solution.carts) == 9
        # This will be a massacre
        solution.tick(return_on_crash=False)
        assert len(solution.carts) == 3

        final_location = solution.tick_until_one_left()
        assert len(solution.carts) == 1
        assert final_location == (6, 4)

    def test_day13b_data(self):
        """Result we got when we did the real solution"""
        solution = Day13PartB()
        res = solution("day_13/day13.txt")
        assert res == (35, 59)
