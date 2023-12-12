from __future__ import annotations

from heapq import heappop, heappush
from typing import Generic, TypeVar

T = TypeVar("T")


class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: list[T] = []

    @property
    def empty(self) -> bool:
        # not is true for empty container
        return not self._container

    def push(self, item: T) -> None:
        # in by priority
        heappush(self._container, item)

    def pop(self) -> T:
        # out by priority
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)

    def __len__(self) -> int:
        return len(self._container)
