from collections import Counter

from adventofcode2021.utils.abstract import FileReaderSolution


class Day06:
    fish: Counter
    day: int

    def tick(self):
        """
        Spawn a new generation of fish!
        """
        self.day += 1
        number_spawning = self.fish[0]

        # Decrease the age of the current population
        new_counter: Counter[int] = Counter()
        for i in range(1, 9):
            new_counter[i - 1] = self.fish[i]

        # And add the new fish
        new_counter[8] = number_spawning

        # Reset the old fish to 6, and add them to the current total
        new_counter[6] += number_spawning
        self.fish = new_counter

    def run(self, input_data: str, num_days: int) -> int:
        self.day = 0
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
