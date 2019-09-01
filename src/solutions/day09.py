from utils.abstract import FileReaderSolution
from collections import Counter
from collections import deque
from tqdm import tqdm


class Day09:
    players = None

    def __init__(self):
        self.players = Counter()
        self.grid = deque()

    def play_game(self, players, last_marble):
        """ Compute the result from the number of `players` and the worth in points
        of the `last_marble`

        :param players: The number of players
        :param last_marble: The last marble is worth so many points
        """
        current_player = 0

        for current_marble in tqdm(range(0, last_marble + 1)):
            current_player += 1
            if current_player > players:
                current_player = 1

            if current_marble > 1 and (current_marble % 23 == 0):
                # Current marble is a multiple of 23!
                # The current player gets the current marble value added to their score
                self.players[current_player] += current_marble
                # the marble 7 marbles counter-clockwise from the current marble is
                # removed from the circle and also added to the current player's score
                self.grid.rotate(7)
                removed_marble = self.grid.popleft()
                self.players[current_player] += removed_marble

            else:
                # Rotate the grid twice
                self.grid.rotate(-2)
                self.grid.appendleft(current_marble)

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
