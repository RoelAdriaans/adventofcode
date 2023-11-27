from collections import Counter

from adventofcode.utils.abstract import FileReaderSolution


class Day06:
    fish: Counter

    def tick(self):
        """
        Spawn a new generation of fish!
        """
        number_spawning = self.fish[0]

        # Decrease the age of the current population
        for i in range(1, 9):
            self.fish[i - 1] = self.fish[i]

        # And add the new fish
        self.fish[8] = number_spawning

        # Reset the old fish to 6, and add them to the current total
        self.fish[6] += number_spawning

    def run(self, input_data: str, num_days: int) -> int:
        self.fish = Counter(int(age) for age in input_data.split(","))
        for _ in range(num_days):
            self.tick()
        return sum(self.fish.values())


class Day06PartA(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.run(input_data, 80)


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        return self.run(input_data, 256)
