from __future__ import annotations

from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container: deque[T] = deque()

    @property
    def empty(self) -> bool:
        # not is true for empty container
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        # FIFO
        return self._container.popleft()

    def __repr__(self) -> str:
        return repr(self._container)
