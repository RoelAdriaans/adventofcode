from __future__ import annotations

import re
from functools import cache
from typing import NamedTuple

from adventofcode.utils.abstract import FileReaderSolution


class Valve(NamedTuple):
    name: str
    connections: list[str]
    flow_rate: int


class Day16:
    valves: dict[str, Valve]

    def parse(self, input_lines: str):
        """Parse lines
        Expected input:

        Valve AA has flow rate=0; tunnels lead to valves DD, II, BB

        """
        self.valves = {}

        parser = re.compile(
            r"Valve (?P<valve>\w*) has flow rate=(?P<flow_rate>\d*); "
            r"tunnel(s?) lead(s?) to valve(s?) (?P<connections>.*)"
        )
        for line in input_lines.splitlines():
            if match := parser.search(line):
                mdict = match.groupdict()
                connections = tuple(c.strip() for c in mdict["connections"].split(","))

                name = mdict["valve"]
                valve = Valve(
                    name, flow_rate=int(mdict["flow_rate"]), connections=connections
                )
                self.valves[name] = valve

            else:
                raise ValueError("Invalid Line", line)

    @cache
    def find_path(
        self,
        current_valve: str,
        time: int,
        open_valves: tuple[str] | None,
        elephant=False,
    ):
        if time == 0:
            # Outatime, Base state, nothing else to compute
            if elephant:
                # Now have the elephant traverse another route
                return self.find_path("AA", 26, open_valves)
            return 0
        # We have 2 options:
        # - Walk to another valve
        # - Open current valve

        # Walk to all the connected valved, this takes one minute.
        max_walking_score = max(
            self.find_path(valve, time - 1, open_valves, elephant)
            for valve in self.valves[current_valve].connections
        )

        # Open the current valve, if there is a flowrate, and it's not yet open
        if (
            self.valves[current_valve].flow_rate > 0
            and current_valve not in open_valves
        ):
            # Add current valve to the open valves
            # Sort the vales
            open_valves = tuple(sorted([*open_valves, current_valve]))

            # Calculate what our flow will be when it's opened
            # e.g. 24 minute left * flow-rate
            current_flow = (time - 1) * self.valves[current_valve].flow_rate
            # Recurse and find a cheaper path
            open_score = current_flow + self.find_path(
                current_valve, time - 1, open_valves, elephant
            )
            return max(open_score, max_walking_score)
        else:
            return max_walking_score


class Day16PartA(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.find_path("AA", 30, (), False)


class Day16PartB(Day16, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        self.parse(input_data)
        return self.find_path("AA", 26, (), True)
