from __future__ import annotations

from adventofcode.utils.abstract import FileReaderSolution


class Day06:
    obstacles: set[tuple[int, int]]
    start_position: tuple[int, int]
    start_direction: int
    max_r: int
    mac_c: int

    def compute_obstables(self, lines):
        self.max_r = len(lines)
        self.max_c = len(lines[0])

        self.obstacles = set()
        for r, row in enumerate(lines):
            for c, cell in enumerate(row):
                if cell == "#":
                    self.obstacles.add((r, c))
                elif cell == "^":
                    self.start_position = (r, c)
                    self.start_direction = 0  # UP

    def path_of_guard(self) -> set[tuple[int, int]]:
        """Get the path of the guard"""
        visited = set()
        directions = [
            (-1, 0),  # UP
            (0, 1),  # RIGHT
            (1, 0),  # DOWN
            (0, -1),  # LEFT
        ]
        current_position = self.start_position
        current_direction = self.start_direction

        # And now work our magic
        total = 0
        max_r = self.max_r
        max_c = self.max_c
        while True:
            c, r = current_position
            # Take a step in the direction
            # current_direction = (current_direction + 1) %4
            cd, rd = directions[current_direction]
            cnew, rnew = c + cd, r + rd
            if (cnew, rnew) in self.obstacles:
                # We have hit something turn right
                current_direction = (current_direction + 1) % 4
                # Get out new loctions
                cd, rd = directions[current_direction]
                cnew, rnew = c + cd, r + rd
            if (cnew, rnew) in self.obstacles:
                raise ValueError("Hit an obstacle")
            # Take a step
            total += 1
            current_position = (cnew, rnew)
            # if current_position in visited:
            #     raise ValueError(f"We have been already at {current_position}")
            visited.add(current_position)
            # Test for outside  boundries:
            # print()
            # inside = 0
            really_visited = set()
            if (cnew > max_c or cnew < 0) or (rnew > max_r or rnew < 0):
                for x in range(max_r):
                    for y in range(max_c):
                        if (x, y) == self.start_position:
                            print("^", end="")
                            really_visited.add((x, y))
                        elif (x, y) in visited:
                            # print("X", end="")
                            # inside += 1
                            really_visited.add((x, y))
                #         elif (x, y) in self.obstacles:
                #             print("#", end="")
                #         else:
                #             print(".", end="")
                #     print()

                # @TODO Refactor really_visited
                return really_visited


class Day06PartA(Day06, FileReaderSolution):

    def solve(self, input_data: str) -> int:
        lines = input_data.splitlines()
        self.compute_obstables(lines)
        return len(self.path_of_guard())


class Day06PartB(Day06, FileReaderSolution):
    def solve(self, input_data: str) -> int:

        lines = input_data.splitlines()
        self.compute_obstables(lines)
        possible_blocks = set()
        for r, c in self.path_of_guard():
            for dr, dc in [
                (-1, 0),  # UP
                (0, 1),  # RIGHT
                (1, 0),  # DOWN
                (0, -1),  # LEFT
            ]:
                possible_blocks.add((r + dr, c + dc))

        counter = 0
        for obstacle in possible_blocks:
            if self.loop_detection(obstacle):
                counter += 1

        return counter

    def loop_detection(self, extra_obstacle) -> bool:
        """Is this grid in a loop?"""
        directions = [
            (-1, 0),  # UP
            (0, 1),  # RIGHT
            (1, 0),  # DOWN
            (0, -1),  # LEFT
        ]
        visited = set()
        obstacles = self.obstacles.copy()
        obstacles.add(extra_obstacle)
        current_position = self.start_position
        current_direction = self.start_direction

        visited.add((current_position, current_direction))
        # And now work our magic
        while True:
            c, r = current_position
            # Take a step in the direction
            # current_direction = (current_direction + 1) %4
            cd, rd = directions[current_direction]
            cnew, rnew = c + cd, r + rd
            if (cnew, rnew) in obstacles:
                # We have hit something turn right
                current_direction = (current_direction + 1) % 4
                # Get out new loctions
                cd, rd = directions[current_direction]
                cnew, rnew = c + cd, r + rd
            # Ieuw, repeated code. Handle walking into an obstacle again.
            # Must be cleaner, to fix.
            if (cnew, rnew) in obstacles:
                # We have hit something turn right
                current_direction = (current_direction + 1) % 4
                # Get out new loctions
                cd, rd = directions[current_direction]
                cnew, rnew = c + cd, r + rd

            if (cnew, rnew) in obstacles:
                raise ValueError("Hit an obstacle after moving again")
            # Take a step
            current_position = (cnew, rnew)
            if (current_position, current_direction) in visited:
                # I've been here before and will come again
                return True

            visited.add((current_position, current_direction))
            # Test for outside boundaries:
            if (cnew > self.max_c or cnew < 0) or (rnew > self.max_r or rnew < 0):
                return False
