from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(
        self,
        state: T,
        parent: Node | None,
        cost: float = 0.0,
        heuristic: float = 0.0,
    ) -> None:
        self.state: T = state
        self.parent: Node | None = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __repr__(self):
        if self.parent:
            parents = self.node_to_path(self)
            return f"{repr(self.state)} <{self.cost}/{self.heuristic}> ({parents})"
        else:
            return f"{repr(self.state)} <{self.cost}/{self.heuristic}>"

    @staticmethod
    def node_to_path(node: Node[T]) -> list[T]:
        path: list[T] = [node.state]

        # work backwards from end to front
        while node.parent is not None:
            node = node.parent
            path.append(node.state)

        path.reverse()
        return path
