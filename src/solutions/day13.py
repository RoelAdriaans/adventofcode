from utils.abstract import FileReaderSolution
from enum import Enum
from typing import List, Tuple


class GridPosition:
    """ Define a simple position on the grid """

    def __init__(self, x: int, y: int, symbol: str, cart: "MineCart" = None):
        """
        Create a new position, based on position (`x`, `y`), and a symbol to
        specify the direction.
        There is no validation on the `symbol`.
        An minecart on this position is possible, but option.
        """
        self.x = x
        self.y = y
        self.symbol = symbol
        if cart:
            self.carts = [cart]
        else:
            self.carts = list()

    def __repr__(self):
        if len(self.carts) == 1:
            symbol = self.carts[0].direction.name
        elif len(self.carts) > 1:
            symbol = "X"
        else:
            symbol = self.symbol
        return f"({self.x}, {self.y}) = {symbol}"

    def is_intersection(self) -> bool:
        """ Is this position an intersection?"""
        if self.symbol == "+":
            return True
        else:
            return False

    def is_straight(self) -> bool:
        if self.symbol in ("|", "-"):
            return True
        else:
            return False

    def is_corner(self) -> bool:
        if self.symbol in ("/", "\\"):
            return True
        else:
            return False

    def has_cart(self):
        """ Return if this grid has a cart """
        if len(self.carts) >= 1:
            return True
        else:
            return False


class Turns(Enum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2

    def get_turn_direction(self, direction: "Direction"):
        """ Compute a new value for direction """
        if self == self.LEFT:
            if direction == Direction.UP:
                return direction.LEFT
            elif direction == Direction.DOWN:
                return direction.RIGHT
            elif direction == Direction.LEFT:
                return direction.DOWN
            elif direction == Direction.RIGHT:
                return direction.UP
        elif self == self.RIGHT:
            if direction == Direction.UP:
                return direction.RIGHT
            elif direction == Direction.DOWN:
                return direction.LEFT
            elif direction == Direction.LEFT:
                return direction.UP
            elif direction == Direction.RIGHT:
                return Direction.DOWN
        elif self == self.STRAIGHT:
            return direction


class Direction(Enum):
    """
    Directions to take with (X, Y) position changes
    X is horizontal, Y is vertical
    """

    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)

    @staticmethod
    def sign_to_direction(direction: str):
        """ Convert a direction ( <, >, ^, v) to a direction """
        if direction == "<":
            return Direction.LEFT
        elif direction == ">":
            return Direction.RIGHT
        elif direction == "v":
            return Direction.DOWN
        elif direction == "^":
            return Direction.UP
        raise ValueError(f"{direction} is not a valid direction")


class MineCart:
    def __init__(self, x: int, y: int, direction: Direction):
        self.last_move = -1
        self.x = x
        self.y = y
        self.direction = direction

    def get_next_move(self):
        self.last_move = (self.last_move + 1) % len(Turns)
        return Turns(self.last_move)

    def _compute_direction(self):
        (delta_x, delta_y) = self.direction.value
        new_x = delta_x + self.x
        new_y = delta_y + self.y
        self.x = new_x
        self.y = new_y

    def set_next_position(self, position: GridPosition):
        """ Get the next position, based on the track and the current direction """
        if position.is_intersection():
            # We are at an intersection.
            new_turn = self.get_next_move()
            self.direction = new_turn.get_turn_direction(self.direction)
            self._compute_direction()

        elif position.is_straight():
            self._compute_direction()

        elif position.is_corner():
            # We are in a corner, for example
            # ^--
            # |
            # We cannot do up, so the only direction is right:
            if self.direction == Direction.UP:
                if position.symbol == "/":
                    self.direction = Direction.RIGHT
                elif position.symbol == "\\":
                    self.direction = Direction.LEFT
            elif self.direction == Direction.DOWN:
                if position.symbol == "/":
                    self.direction = Direction.LEFT
                elif position.symbol == "\\":
                    self.direction = Direction.RIGHT
            elif self.direction == Direction.RIGHT:
                if position.symbol == "/":
                    self.direction = Direction.UP
                elif position.symbol == "\\":
                    self.direction = Direction.DOWN
            elif self.direction == Direction.LEFT:
                if position.symbol == "/":
                    self.direction = Direction.DOWN
                elif position.symbol == "\\":
                    self.direction = Direction.UP

            self._compute_direction()

        else:
            raise ValueError("Cannot compute position!")


class Day13:
    def __init__(self):
        self.grid = dict()
        self.carts = list()

    def build_grid(self, lines: List[str]):
        for y, line in enumerate(lines):
            for x, symbol in enumerate(line):
                if not symbol.strip():
                    continue
                if symbol in ("<", ">", "v", "^"):
                    minecart = MineCart(
                        x, y, direction=Direction.sign_to_direction(symbol)
                    )
                    self.carts.append(minecart)
                    if symbol in ("<", ">"):
                        symbol = "-"
                    else:
                        symbol = "|"
                else:
                    # No minecart at this position
                    minecart = None

                pos = GridPosition(x, y, symbol, minecart)
                self.grid[(x, y)] = pos

    def tick(self):
        """ Run the simulation for one tick. """
        seen_carts = set()
        for grid_position, position in self.grid.items():
            if position.has_cart() and position.carts[0] not in seen_carts:
                # Add cart to seen cart, and remove it from the current grid
                cart = position.carts[0]
                seen_carts.add(position.carts[0])
                position.carts = list()

                # We skip the intersections for now.
                # We skip turns for now.

                cart.set_next_position(position)
                self.grid[(cart.x, cart.y)].carts.append(cart)
                if len(self.grid[(cart.x, cart.y)].carts) >= 2:
                    return cart.x, cart.y
        else:
            return False

    def ticks(self, n=1):
        """ Do `n` ticks"""
        for _ in range(n):
            colission = self.tick()
            if colission:
                return colission


class Day13PartA(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        self.build_grid(lines=lines)
        while True:
            colission = self.tick()
            if colission:
                return colission


class Day13PartB(Day13, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
