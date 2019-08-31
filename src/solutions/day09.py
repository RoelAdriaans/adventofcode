from typing import Dict

from utils.abstract import FileReaderSolution
from collections import defaultdict, Counter
from tqdm import tqdm


class Day09:
    players = None

    def __init__(self):
        self.players = Counter()
        self.grid = list()
        self.current_marble = 0
        self.available_marbles = list()

    def _compute_position(self) -> int:
        """
        Returns the position for the new marble that is going to be places in the grid.

        Now we have to compute the positions.
        Each Elf takes a turn placing the lowest-numbered remaining marble into
        the circle between the marbles that are 1 and 2 marbles clockwise of the
        current marble.
        (When the circle is large enough, this means that there is one marble between
        the marble that was just placed and the current marble.) The marble that was
        just placed then becomes the current marble.

        This is based on the `self.current_marble`. That is the last marble that is
        played.
        :return:
        """
        grid_size = len(self.grid)
        if grid_size == 0:
            return 0
        if grid_size == 1:
            return 1

        raise ValueError("Not suited for this value")

    def _compute_position_from_previous(self, previous_position: int) -> int:
        """
        Simple compute of the previous position
        """
        return self._get_index(previous_position + 2)

    def _get_index(self, position: int) -> int:
        """
        Return the index in the grid for a position. If the posisition is outside
        the grid, the index will be reset
        """
        if position < 0:
            # position = len(self.grid) - position
            # return position
            raise ValueError("Negative not supported!")

        grid_size = len(self.grid)
        if position == grid_size:
            # If we are on the right edge, return this value
            return position

        current_index = position % grid_size
        return current_index

    def _remove_marble(self, current_index):
        """
        Remove marble 7 positions from the `current_marble` and
        update `current_marble` with the new position

        :return: The value of the removed marble
        """
        next(self.available_marbles)
        score = self.current_marble

        if current_index < 7:
            # Eerst de rest:
            left = 7 - current_index
            search_index = len(self.grid) - left
        else:
            search_index = current_index - 7
        remove_position = self._get_index(search_index)

        # Add the value of that marble to the score
        score += self.grid[remove_position]

        # Current marble the is next to the one we removed just now
        self.current_marble = self.grid[remove_position + 1]

        self.grid.pop(remove_position)

        return score, remove_position

    def _insert_marble(self, position: int) -> int:
        """
        Insert the first abailable marble at the position `position`.
        If a marble is already at this position, it will be shifted to the right.

        Begin state:
        0 2 1 3
        Insert marble 4 at position 1:
        0 4 2 1 3

        :param position: Position to add the marble to
        :return: The value of the marble that was added
        """
        try:
            marble = next(self.available_marbles)
        except StopIteration:
            return False
        self.grid.insert(position, marble)
        return marble

    def play_game(self, players, last_marble):
        """ Compute the result from the number of `players` and the worth in points
        of the `last_marble`

        :param players: The number of players
        :param last_marble: The last marble is worth so many points
        """
        self.current_marble = 0
        self.available_marbles = iter(range(0, last_marble + 1))
        current_player = 0

        # Ad the first marble to the board
        position = self._compute_position()
        previous_position = position
        self._insert_marble(position=position)

        pbar = tqdm(total=last_marble + 1, ncols=120)

        while True:
            pbar.update(1)

            if self.current_marble >= last_marble:
                pbar.close()
                return

            current_player += 1
            if current_player > players:
                current_player = 1

            # We need to figure out where to place the next marble
            # position = self._compute_position()
            if previous_position:
                # If we have a previuos position, use this to compute the next one
                position = self._compute_position_from_previous(previous_position)
            else:
                # Sometimes we cannot do this, for example when a marble has been
                # removed
                position = self._compute_position()

            self.current_marble += 1

            if self.current_marble > 1 and (self.current_marble % 23 == 0):
                # Current marble is a multiple of 23!
                # The current player gets the current marble value added to their score

                # Remove the marble, add this value to the score
                score, previous_position = self._remove_marble(previous_position)
                self.players[current_player] += score

            else:
                self.current_marble = self._insert_marble(position=position)
                if not self.current_marble:
                    return
                previous_position = position

    def compute_result(self, players: int, last_marble: int) -> int:
        """
        Compute the result from the number of `players` and the worth in points
        of the `last_marble`

        :param players: The number of players
        :param last_marble: The last marble is worth so many points
        :returns the highest score
        """
        self.play_game(players, last_marble)
        return self.compute_score()

    def compute_score(self) -> int:
        """ Compute the score for a player"""
        best_player = self.players.most_common(1)
        return best_player[0][1]


class Day09PartA(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        input_data = input_data.split()
        players = int(input_data[0])
        marble = int(input_data[6])
        score = self.compute_result(players=players, last_marble=marble)
        return score


class Day09PartB(Day09, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        input_data = input_data.split()
        players = int(input_data[0])
        marble = int(input_data[6]) * 100
        score = self.compute_result(players=players, last_marble=marble)
        return score
