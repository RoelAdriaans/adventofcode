from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import TypeVar

from adventofcode2022.utils.node import Node
from adventofcode2022.utils.priority_queue import PriorityQueue
from adventofcode2022.utils.queue import Queue
from adventofcode2022.utils.stack import Stack

T = TypeVar("T")

# @TODO: Make the container a protocol?
Container = Queue | Stack


class Search(ABC):
    @abstractmethod
    def _get_container(self) -> Container:
        """Return the base container for this class"""
        raise NotImplementedError

    def search(
        self,
        initial: T,
        goal_test: Callable[[T], bool],
        successors: Callable[[T], list[T]],
    ) -> Node[T] | None:
        # frontier is where we've yet to go
        # @TODO This is ugly, the base class has knowledge of
        #   the container implementation
        frontier: Queue[Node[T]] | Stack[Node[T]] = self._get_container()
        frontier.push(Node(initial, None))

        # explored is where we've been
        explored: set[T] = {initial}

        # keep going while there is more to explore
        while not frontier.empty:
            current_node: Node[T] = frontier.pop()
            current_state: T = current_node.state

            # if we found the goal, we're done
            if goal_test(current_state):
                return current_node

            # check where we can go next and haven't explored
            for child in successors(current_state):
                if child in explored:
                    # skip children we already explored
                    continue
                explored.add(child)
                frontier.push(Node(child, current_node))

        # went through everything and never found goal
        return None


class DFS(Search):
    """Perform a Depth-first search (DFS)"""

    def _get_container(self) -> Container:
        return Stack()


class BFS(Search):
    """Perform a Breadth-first search (BFS)"""

    def _get_container(self) -> Container:
        return Queue()


class Astar:
    @staticmethod
    def astar(
        initial: T,
        goal_test: Callable[[T], bool],
        successors: Callable[[T], list[T]],
        heuristic: Callable[[T], float],
    ) -> Node[T] | None:
        # frontier is where we've yet to go
        frontier: PriorityQueue[Node[T]] = PriorityQueue()
        frontier.push(Node(initial, None, 0.0, heuristic(initial)))

        # explored is where we've been
        explored: dict[T, float] = {initial: 0.0}

        # keep going while there is more to explore
        while not frontier.empty:
            current_node: Node[T] = frontier.pop()
            current_state: T = current_node.state
            # if we found the goal, we're done
            if goal_test(current_state):
                return current_node
            # check where we can go next and haven't explored
            for child in successors(current_state):
                # 1 assumes a grid, need a cost function for more sophisticated apps
                new_cost: float = current_node.cost + 1

                if child not in explored or explored[child] > new_cost:
                    explored[child] = new_cost
                    frontier.push(Node(child, current_node, new_cost, heuristic(child)))

        # went through everything and never found goal
        return None
