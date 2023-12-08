from typing import List

import tqdm

from utils.abstract import FileReaderSolution


class Elve:
    def __init__(self, current_recipe: int, current_recipe_idx: int):
        self.current_recipe = current_recipe
        self.current_recipe_idx = current_recipe_idx

    def __repr__(self):
        return f"Working on {self.current_recipe}"


class Day14:
    """Day 14: Chocolate Charts"""

    scoreboard = list()
    elves = list()

    def parse_data(self, input_data: str):
        """
        Parse the data in `input_data` as scoreboard
        :param input_data:
        :return:
        """
        self.scoreboard = [int(x) for x in list(input_data)]

    def compute_new_recipes(self) -> list[int]:
        """
        Based on the scoreboard and elves, compute new scores.

        If the elves are working on recipes 3 and 7, the sum will be 10 and the result
        will be two recipes, 1 and 0.
        IF the elves are working on recipes 2 and 3, the sum will be 5 and the result
        will be one recipe, 5
        """
        sum_of_digits = sum([elve.current_recipe for elve in self.elves])
        return [int(d) for d in str(sum_of_digits)]

    def initalise(self, input_data: str, num_elves: int):
        """
        Parse the data and create the elve
        :param input_data: String of numbers
        :param num_elves: The number of elves available
        :return: String with the score.
        """
        # Cleanup, in testing we instantieace
        self.elves = list()
        self.scoreboard = list()
        self.parse_data(input_data)

        # Create `num_elves` with the first recipes from the scoreboard
        for recipe_index in range(num_elves):
            elve = Elve(self.scoreboard[recipe_index], recipe_index)
            self.elves.append(elve)

    def pick_new_recipe(self):
        """
        Let the elves pick a new recipe
        :return:
        """
        for elve in self.elves:
            steps_forward = elve.current_recipe + 1
            new_idx = (elve.current_recipe_idx + steps_forward) % len(self.scoreboard)
            elve.current_recipe_idx = new_idx
            elve.current_recipe = self.scoreboard[new_idx]
            pass

    def compute_next_recipes(self, num_recipes: int):
        """
        Compute the score of the final recipes after `num_recipes` tries
        """
        for _ in range(num_recipes):
            new_recipes = self.compute_new_recipes()
            self.scoreboard.extend(new_recipes)

            # Compute new recipe for the elves
            self.pick_new_recipe()

    def compute_recipe_length(self, num_recipes_created: int):
        """
        Run until we have created `num_recipes_created`
        :param num_recipes_created:
        :return:
        """
        while len(self.scoreboard) < num_recipes_created:
            self.compute_next_recipes(1)

    def total_score(self, after_num_recipes) -> str:
        """
        Return the total score after `after_num_recipes`
        """
        start = after_num_recipes
        stop = after_num_recipes + 10
        numbers = self.scoreboard[start:stop]
        result = "".join([str(number) for number in numbers])
        return result

    @staticmethod
    def find_sequence_in_list(needle: list, haystack: list) -> int:
        """
        Search for the list `needle` in `haystack`, and return offset from the
        end where we search. If the needle is not found, return False

        We only search at the end, or one or  two records before the end.
        Eg: [2, 3] is in [2, 3, 4] and returns 1
        Eg: [3, 4] is in [2, 3, 4] and returns 0

        :param needle:
        :param haystack:
        :return: Offset
        """
        length_needle = len(needle)
        last_digits = haystack[-length_needle:]
        # Check for the last position
        if last_digits == needle:
            return 0
        # Check for the first to last position
        last_digits = haystack[-(length_needle + 1) : -1]
        if last_digits == needle:
            return 1
        # Check for the second to last position
        last_digits = haystack[-(length_needle + 2) : -2]
        if last_digits == needle:
            return 2
        return False

    def search_for_recipe(self, recipe: str) -> int:
        """
        Alves had it backwards, and we now want to search for `recipe`, and return
        after how many recipes it is in the list
        :param recipe:
        :return:
        """
        # for recipe_step in count(0):
        recipe_digits = [int(digit) for digit in list(recipe)]
        num_digits = len(recipe_digits)
        for _ in tqdm.tqdm(range(20235240)):
            self.compute_next_recipes(1)
            result = self.find_sequence_in_list(
                needle=recipe_digits, haystack=self.scoreboard
            )
            if result:
                return len(self.scoreboard) - num_digits - result

        raise ValueError("There should have been a solution now...")


class Day14PartA(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        # We hardcode the number of elves to two, this is in the original assignment
        self.initalise(input_data="37", num_elves=2)
        # Recipes needed is the also the number of our puzzle input
        num_recipes = int(input_data)
        self.compute_recipe_length(num_recipes + 10)
        score = self.total_score(num_recipes)

        return score


class Day14PartB(Day14, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        # We hardcode the puzzle input, since it's not in the input we're given
        self.initalise(input_data="37", num_elves=2)

        result = self.search_for_recipe(input_data)
        return result
