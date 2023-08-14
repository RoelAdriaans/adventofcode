from __future__ import annotations

import itertools

from adventofcodeutils.generic_search import BFS, Astar

from adventofcode2016.utils.abstract import FileReaderSolution


class FacilityState:
    """Current state of the facility"""

    floors: list[list[str]]
    all_objects: list[str]

    def __init__(self, floors: list[list[str]]) -> None:
        """Create a new state of the Facility.

        Args:
            floors: All the objects on floors
        """
        self.floors = floors
        self.all_objects = list(itertools.chain(*floors))
        if "elevator" not in self.all_objects:
            raise ValueError("Elevator not found!")

    def __eq__(self, other: FacilityState) -> bool:
        return hash(self) == hash(other)
        # return self.floors == other.floors and self.all_objects == other.all_objects

    def __hash__(self):
        # Convert the floors to tuples to make it hashable
        # return hash(tuple(tuple(x) for x in self.floors))
        lst = []
        for floor in self.floors:
            lst.append(tuple(item.split()[0] for item in sorted(floor)))
        return hash(tuple(lst))

    def goal_test(self) -> bool:
        """Validate that we are in the end-state, and that this is a legal setting."""
        return self.is_legal and len(self.floors[3]) == len(self.all_objects)

    @staticmethod
    def _test_is_legal(floor: list[str]) -> bool:
        generators = {item.split()[0] for item in floor if item.endswith("generator")}
        chips = {item.split()[0] for item in floor if item.endswith("chip")}

        if not generators:
            # No generators, nothing to check
            return True

        for chip in chips:
            if chip in generators:
                # We have a chip-generator combo:
                pass
            else:
                return False

        return True

    @property
    def is_legal(self) -> bool:
        """Is this state legal?

        If a chip is ever left in the same area as another RTG, and it's not connected
        to its own RTG, the chip will be fried.

        Therefore, it is assumed that you will follow procedure and keep chips
        connected to their corresponding RTG when they're in the same room, and away
        from other RTGs otherwise.
        """
        return all(self._test_is_legal(floor) for floor in self.floors)

    @property
    def elevator(self) -> int:
        for idx, floor in enumerate(self.floors):
            if "elevator" in floor:
                return idx
        raise IndexError

    def list_of_items_from_floor(self, floor: int) -> list[tuple[str]]:
        """Take items from floor `floor`. Skip the elevator. Returns 1 or 2 items"""

        items = set(self.floors[floor])
        # Move everything except the elevator, if it exists
        items.discard("elevator")

        combinations = list(
            itertools.chain(
                itertools.combinations(items, 1),
                itertools.combinations(items, 2),
            )
        )
        # Validate the set in the elevator
        valid = [
            combination
            for combination in combinations
            if self._test_is_legal(combination)
        ]
        return valid

    def successors(self) -> list[FacilityState]:
        """The list of successors from this state.

        We can:
        - move 1 or 2 things
        - not move a generator and a microchip at the same time, if they are different
        - The elevator stops on every floor
        - If the elevator stops - the state must be valid
        """
        sucs: list[FacilityState] = []

        # From the current floor, where the elevator is, we can move 1 or 2 things
        current_floor = self.elevator

        destination_floors = []
        if current_floor > 0:
            destination_floors.append(current_floor - 1)
        if current_floor < len(self.floors) - 1:
            destination_floors.append(current_floor + 1)

        for destination in destination_floors:
            items_to_move = self.list_of_items_from_floor(current_floor)
            # New state: Move items from `items_to_move` to floor `destination`
            for items in items_to_move:
                ns = self.copy()
                for item in items:
                    ns.floors[current_floor].remove(item)
                    ns.floors[destination].append(item)
                ns.floors[current_floor].remove("elevator")
                ns.floors[destination].append("elevator")
                if ns.is_legal:
                    sucs.append(ns)

        return sucs

    def __str__(self) -> str:
        ret = []
        for idx, floor in enumerate(reversed(self.floors)):
            elements = ", ".join(self.str_element(element) for element in floor)
            ret.append(f"F{len(self.floors) - idx} {elements}".strip())
        return "\n".join(ret)

    @staticmethod
    def str_element(element: str) -> str:
        """Create a short-form for an element"""
        if element == "elevator":
            return "ELEV"
        parts = element.split()
        return f"{parts[0]}-{parts[-1]}"
        # return f"{parts[0][:2].upper()}{parts[-1][:2].lower()}"

    def heuricstic(self) -> int:
        return len(self.floors[3]) - len(self.all_objects)

    def diff(self, prev: FacilityState) -> str:
        res = []
        for idx, floor in enumerate(self.floors):
            res.append(f"F{len(self.floors) - idx}")
            cur = set(floor)
            oht = set(prev.floors[idx])
            if add := cur.difference(oht):
                res.append(f"+++ {', '.join(self.str_element(itm) for itm in add)}")
            if sub := oht.difference(cur):
                res.append(f"--- {', '.join(self.str_element(itm) for itm in sub)}")

        return "\n".join(res)

    def copy(self) -> FacilityState:
        new_floors = [floor[:] for floor in self.floors]
        return FacilityState(new_floors)


class Day11:
    def parse(self, input_data: str) -> FacilityState:
        floors = []

        for line in input_data.splitlines():
            floor = []

            parts = line.split()
            name = None
            for part in parts[5:]:
                if part in ("and", ",", "a", "relevant."):
                    continue

                if name is None:
                    name = part.rstrip(",.").replace("-compatible", "").strip()
                else:
                    # We name and type:
                    floor.append(f"{name} {part.rstrip(',.').strip()}")
                    name = None

            floors.append(floor)

        # When you enter the containment area, you and the elevator will start on the
        # first floor.
        floors[0].insert(0, "elevator")

        return FacilityState(floors=floors)


class Day11PartA(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        start_state = self.parse(input_data)
        path = BFS().search(
            initial=start_state,
            goal_test=FacilityState.goal_test,
            successors=FacilityState.successors,
        )
        return len(path.node_to_path(path)) - 1


class Day11PartB(Day11, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        start_state = self.parse(input_data)

        start_state.floors[0].append("elerium generator")
        start_state.floors[0].append("elerium microchip")
        start_state.floors[0].append("dilithium generator")
        start_state.floors[0].append("dilithium microchip")

        path = Astar().astar(
            initial=start_state,
            goal_test=FacilityState.goal_test,
            successors=FacilityState.successors,
            heuristic=FacilityState.heuricstic,
        )
        return len(path.node_to_path(path)) - 1
