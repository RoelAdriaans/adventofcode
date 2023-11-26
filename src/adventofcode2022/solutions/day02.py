from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class RPC:
    shape: str
    score: int
    wins_from: list[RPC]

    def __init__(self, shape: str, score: int):
        self.shape = shape
        self.score = score
        self.wins_from = []

    def __repr__(self):
        return f"RPC({self.shape} {self.score})"

    def add_wins(self, rpc: RPC):
        self.wins_from.append(rpc)

    def wins(self, other):
        """Check if other wins from us, and return this as a boolean"""
        return other in self.wins_from


class Day02:
    games: dict[str, RPC]

    @staticmethod
    def create_types() -> dict[str, RPC]:
        """Create al the possible types, wins and scores for the types"""
        rpc_types: dict[str, RPC] = {
            "A": RPC("Rock", 1),
            "B": RPC("Paper", 2),
            "C": RPC("Scissors", 3),
            "X": RPC("Rock", 1),
            "Y": RPC("Paper", 2),
            "Z": RPC("Scissors", 3),
        }

        # Rock wins from Scissors
        rpc_types["A"].add_wins(rpc_types["Z"])
        rpc_types["X"].add_wins(rpc_types["C"])

        # Paper wins from Rock
        rpc_types["B"].add_wins(rpc_types["X"])
        rpc_types["Y"].add_wins(rpc_types["A"])

        # Sciccors wins from Paper
        rpc_types["C"].add_wins(rpc_types["Y"])
        rpc_types["Z"].add_wins(rpc_types["B"])

        return rpc_types

    @staticmethod
    def play_game(games: list[tuple[RPC, RPC]]) -> tuple[int, int]:
        score_p1, score_p2 = 0, 0
        for p1, p2 in games:
            if p1.shape == p2.shape:
                # It's a draw
                score_p1 += 3 + p1.score
                score_p2 += 3 + p2.score
            elif p1.wins(p2):
                score_p1 += 6 + p1.score
                score_p2 += p2.score
            elif p2.wins(p1):
                score_p2 += 6 + p2.score
                score_p1 += p1.score
            else:
                score_p1 += p1.score
                score_p2 += p2.score
                print(f"It's a draw between {p1} and {p2}")
        return score_p1, score_p2


class Day02PartA(Day02, FileReaderSolution):
    def parse(self, input_data: str) -> list[tuple[RPC, RPC]]:
        """Create a list of games played"""
        games: list[tuple[RPC, RPC]] = []
        rpc_types = self.create_types()
        for game in input_data.splitlines():
            p1, p2 = game.split()
            games.append((rpc_types[p1], rpc_types[p2]))

        return games

    def solve(self, input_data: str) -> int:
        games = self.parse(input_data)
        _, score_p2 = self.play_game(games)
        return score_p2


class Day02PartB(Day02, FileReaderSolution):
    @staticmethod
    def find_loose(rpc_types, rpc: RPC) -> RPC:
        if rpc.shape == "Rock":
            return rpc_types["Z"]  # Scissors
        elif rpc.shape == "Paper":
            return rpc_types["X"]  # Rock
        elif rpc.shape == "Scissors":
            return rpc_types["Y"]  # Paper
        raise ValueError("Unknown type ", rpc.shape)

    @staticmethod
    def find_win(rpc_types, rpc: RPC) -> RPC:
        if rpc.shape == "Rock":
            return rpc_types["Y"]
        elif rpc.shape == "Paper":
            return rpc_types["Z"]
        elif rpc.shape == "Scissors":
            return rpc_types["X"]
        raise ValueError("Unknown type ", rpc.shape)

    @staticmethod
    def find_draw(rpc_types, rpc: RPC) -> RPC:
        if rpc.shape == "Rock":
            return rpc_types["X"]
        elif rpc.shape == "Paper":
            return rpc_types["Y"]
        elif rpc.shape == "Scissors":
            return rpc_types["Z"]
        raise ValueError("Unknown type ", rpc.shape)

    def parse(self, input_data: str) -> list[tuple[RPC, RPC]]:
        """Create a list of games played"""
        games: list[tuple[RPC, RPC]] = []
        rpc_types = self.create_types()
        for game in input_data.splitlines():
            p1, p2 = game.split()
            if p2 == "X":
                # Loose
                rpc_p2 = self.find_loose(rpc_types, rpc_types[p1])
            elif p2 == "Y":
                # Draw
                rpc_p2 = self.find_draw(rpc_types, rpc_types[p1])
            else:
                # Win
                rpc_p2 = self.find_win(rpc_types, rpc_types[p1])
            games.append((rpc_types[p1], rpc_p2))
        return games

    def solve(self, input_data: str) -> int:
        games = self.parse(input_data)
        _, score_p2 = self.play_game(games)
        return score_p2
