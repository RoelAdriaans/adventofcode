from collections import defaultdict
from typing import Literal, Union

from adventofcode2021.utils.abstract import FileReaderSolution


class Number:
    number: int
    picked: bool

    def __init__(self, number: int):
        self.number = number
        self.picked = False

    def __repr__(self):
        if self.picked:
            return f"*{self.number:2}*"
        else:
            return f" {self.number:2}"


class Board:
    board: dict[int, dict[int, Number]]

    def __init__(self, string: list[str]):
        """Create a bingo board"""
        self.board = defaultdict(dict)
        for row, line in enumerate(string):
            for col, value in enumerate(int(s) for s in line.split() if s.isdigit()):
                self.board[row][col] = Number(value)

    def draw(self, number):
        for x in self.board.values():
            for y in x.values():
                if y.number == number:
                    y.picked = True

    def is_winner(self) -> bool:
        # Check horizontal win
        for x in self.board.values():
            val = all(n.picked for n in x.values())
            if val:
                return True
        # Check vertital win:
        for y in range(5):
            if all([x[y].picked for x in self.board.values()]):
                return True
        return False

    def unmarked_numbers(self) -> int:
        total = 0
        for x in self.board.values():
            for y in x.values():
                if not y.picked:
                    total += y.number
        return total


class Day04:
    boards: list[Board]
    random_numbers: list[int]

    def read_input(self, input_data):
        lines = input_data.splitlines()
        self.boards = []
        self.random_numbers = [int(num) for num in lines[0].split(",")]

        for board_start in range(2, len(lines) - 2, 6):
            board_text = lines[board_start : board_start + 5]
            board = Board(board_text)
            self.boards.append(board)

    def is_winner(self) -> Union[Literal[False], Board]:
        """Do we have any wining boards?"""
        for board in self.boards:
            if board.is_winner():
                return board
        return False

    def all_won(self):
        return all(board.is_winner() for board in self.boards)

    def draw(self, number):
        for board in self.boards:
            board.draw(number)


class Day04PartA(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.read_input(input_data)

        number = -1
        won_board: Union[Literal[False], Board] = False

        for number in self.random_numbers:
            self.draw(number)
            if won_board := self.is_winner():
                break

        # Winner winner, chicken dinner!
        # Find the sum of all unmarked numbers
        if won_board:
            unmarked = won_board.unmarked_numbers()
            return unmarked * number
        else:
            return -1


class Day04PartB(Day04, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.read_input(input_data)

        last_won: Union[Literal[False], Board] = False
        number = -1
        already_won = set()
        for number in self.random_numbers:
            self.draw(number)
            for board in self.boards:
                if board.is_winner() and board not in already_won:
                    last_won = board

            if self.all_won():
                break

            # We're not done yet, to let's add all the boards that have won on this
            # round to the set
            for board in self.boards:
                if board not in already_won and board.is_winner():
                    already_won.add(board)

        # Winner winner, chicken dinner!
        # Find the sum of all unmarked numbers
        if last_won:
            unmarked = last_won.unmarked_numbers()
            return unmarked * number
        else:
            return -1
