from adventofcodeutils import parsing

from adventofcode.utils.abstract import FileReaderSolution


class Day05:
    @staticmethod
    def parse(input_data: str):
        input_rules, input_pages_to_produce = input_data.split("\n\n")
        rules: list[tuple[int, int]] = []
        pages: list[list[int]] = []
        for rule in input_rules.splitlines():
            x, y = parsing.extract_digits_from_string(rule)
            rules.append((x, y))

        for page in input_pages_to_produce.splitlines():
            pages.append(parsing.extract_digits_from_string(page))
        return rules, pages

    @staticmethod
    def is_right_order(rules, update) -> int:
        for idx, number in enumerate(update):
            # First find all the rules that match this update
            matches = [x for x in rules if x[0] == number and x[1] in update]
            # Find out that all the numbers behind our number are behind us
            for match in matches:
                if match[1] in update[0:idx]:
                    return False
        return True


class Day05PartA(Day05, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        rules, pages = self.parse(input_data)
        total = 0
        for page in pages:
            if self.is_right_order(rules, page):
                total += page[len(page) // 2]
        return total


class Day05PartB(Day05, FileReaderSolution):
    @staticmethod
    def find_broken_index(rules, update) -> tuple[int, tuple[int, int]]:
        for idx, number in enumerate(update):
            # First find all the rules that match this update
            matches = [x for x in rules if x[0] == number and x[1] in update]
            # Find out that all the numbers behind our number are behind us
            for match in matches:
                if match[1] in update[0:idx]:
                    return idx, match
        raise ValueError("Only feed be broken pages")

    def fix_page(self, rules, page):
        # Brute force fixing this page by swapping some values
        # Could be cleaner, but this runs in about 1.5 seconds
        while not self.is_right_order(rules, page):
            # Fix the page. First, find the index that is not correct
            broken_index, broken_match = self.find_broken_index(rules, page)
            # Now we have to find out how we can fix this.
            bad_idx = page.index(broken_match[0])
            other_idx = page.index(broken_match[1])
            page[bad_idx], page[other_idx] = page[other_idx], page[bad_idx]
        return page

    def solve(self, input_data: str) -> int:
        rules, pages = self.parse(input_data)
        total = 0
        for page in pages:
            if not self.is_right_order(rules, page):
                # Fix page
                fixed_page = self.fix_page(rules, page)
                total += page[len(fixed_page) // 2]
        return total
