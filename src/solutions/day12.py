from utils.abstract import FileReaderSolution
import itertools

""" 
Game of live. Do we model the plants, or do we model the list?

If we model the plants, we can just do a for loop over the plants, but we need an 
effecient way to get the neightbours. 

If we model the 'table', we can loop over the table, pick out the plants and we have 
the neight plants surounding them.

Table is it. 
  
"""


class Garden:
    PLANT = "#"
    EMPTY = "."

    def __init__(self, spots: list = None):
        # We use the offset to do negative indexing
        self.offset = 5

        self.table = ["."] * self.offset + spots + ["."] * self.offset
        self.notes = dict()
        self.generation = 0

    def split_notes(self, notes: list = None):
        """ Parse the notes in `notes` and store them

        :param notes: The notes we found with information
        """
        for note in notes:
            parts = note.split(" => ")
            if len(parts) == 2 and parts[1].strip() == "#":
                self.notes[parts[0].strip()] = True

        # Fill the empty spots in with False
        options = list(itertools.product("#.", repeat=5))
        for option in options:
            option_string = "".join(option)
            if option_string not in self.notes:
                self.notes[option_string] = False

    def __repr__(self):
        return self.EMPTY * 5 + "".join(self.table) + self.EMPTY * 5

    def generate(self, num_generations=1):
        """ Generate a `num_generations` new generations of plants """

        # Loop over all the spots, but we need to get the ones to the left as well.
        #
        # Generate a new empty table, with space in the front and back
        for _ in range(num_generations):
            self.generation += 1
            next_gen = ["."] * (10 + len(self.table))
            for center_point in range(2, len(self.table) - 2):
                left = center_point - 2
                right = center_point + 3
                plants = self.table[left:right]
                plant_string = "".join(plants)
                do_we_live = self.notes[plant_string]
                if do_we_live:
                    next_gen[center_point] = self.PLANT
                else:
                    next_gen[center_point] = self.EMPTY
            last_plant = "".join(next_gen).rindex(self.PLANT)
            self.table = next_gen[: last_plant + 5]

    def count_plants(self) -> int:
        """ Count the numbers of the spots containing the plants"""
        return sum(
            [i - self.offset for i, x in enumerate(self.table) if x == self.PLANT]
        )


class Day12:
    pass


class Day12PartA(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.split("\n")
        initial_state = list(lines[0].split()[2])
        garden = Garden(initial_state)
        garden.split_notes(lines[1:])
        garden.generate(20)
        return garden.count_plants()


class Day12PartB(Day12, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
