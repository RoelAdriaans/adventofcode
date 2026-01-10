from collections import Counter

from adventofcode.utils.abstract import FileReaderSolution


class Day02:
    pass


class Day02PartA(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        valid_games = 0

        for line in input_data.splitlines():
            line = line.replace(":", "").replace(";", "").replace(",", "")

            parts = line.split()
            game_id = int(parts[1])
            is_valid = True
            for number_idx in range(2, len(parts), 2):
                colors = Counter()
                color_idx = number_idx + 1
                colors[parts[color_idx]] += int(parts[number_idx])

                if (
                    colors["red"] <= 12
                    and colors["green"] <= 13
                    and colors["blue"] <= 14
                ):
                    pass
                else:
                    is_valid = False
            if is_valid:
                valid_games += game_id
        return valid_games


class Day02PartB(Day02, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        total = 0

        for line in input_data.splitlines():
            line = line.replace(":", "").replace(";", "").replace(",", "")

            parts = line.split()
            max_colors = {
                "red": False,
                "green": False,
                "blue": False,
            }

            for number_idx in range(2, len(parts), 2):
                color_idx = number_idx + 1
                color = parts[color_idx]
                number = int(parts[number_idx])

                # Check if the number is the lowest
                if not max_colors[color]:
                    max_colors[color] = number
                else:
                    max_colors[color] = max(max_colors[color], number)
            res = max_colors["red"] * max_colors["green"] * max_colors["blue"]
            total += res
        return total
