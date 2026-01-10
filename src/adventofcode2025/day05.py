import logging

from adventofcode.utils.abstract import FileReaderSolution

_logger = logging.getLogger(__name__)


class Day05:
    ranges: list[range]
    ingredients: list[int]

    def create_ranges_and_ingredients(self, input_data: str):
        ranges, ingredients = input_data.split("\n\n")
        self.ranges = []
        self.ingredients = []
        for range_ in ranges.splitlines():
            min_range, max_range = range_.split("-")
            self.ranges.append(range(int(min_range), int(max_range) + 1))
        self.ranges = sorted(self.ranges, key=lambda r: r[0])
        self.ingredients = [int(ingredient) for ingredient in ingredients.splitlines()]


class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_ranges_and_ingredients(input_data)

        fresh_ingredients = 0

        for ingredient in self.ingredients:
            ingredient_value = int(ingredient)
            if any(ingredient_value in range_ for range_ in self.ranges):
                fresh_ingredients += 1
        return fresh_ingredients


class Day05PartB(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.create_ranges_and_ingredients(input_data)

        # We need to manage a list of start and end ranges. When we see a new range,
        # we have to either expand one of the existing ranges, or add a new one.
        ranges: list[tuple[int, int]] = []
        # Ranges is a list of tuples, with a start and stop range.
        for range_ in self.ranges:
            start = range_.start
            end = range_.stop - 1  # inclusive
            merged = False
            for i, (existing_start, existing_end) in enumerate(ranges):
                if start <= existing_end + 1 and end >= existing_start - 1:
                    # Merge the ranges
                    new_start = min(existing_start, start)
                    new_end = max(existing_end, end)
                    ranges[i] = (new_start, new_end)
                    merged = True
                    break
            if not merged:
                ranges.append((start, end))

        # Now we have a list of merged ranges, we can find number of valid ingredients
        _logger.debug("Finished comuting ranges, found %s", len(ranges))

        # And cound the numbers between the ranges
        valid_ingredients = 0
        for start, end in ranges:
            valid_ingredients += end - start + 1
        return valid_ingredients
