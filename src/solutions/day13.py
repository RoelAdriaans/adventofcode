from utils.abstract import FileReaderSolution
from enum import Enum


class Turns(Enum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2


class Direction(Enum):
    """
    Directions to take with (X, Y) position changes
    X is horizontal, Y is vertical
    """
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)


class MineCart:

    def __init__(self):
        self.last_move = -1

    def get_next_move(self):
        self.last_move = (self.last_move + 1) % len(Turns)
        return Turns(self.last_move)


class Day13:
    def build_grid(self, input_data:str ):
        pass


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()




class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
