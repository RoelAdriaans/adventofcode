from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: list[T] = []

    @property
    def empty(self) -> bool:
        # not is true for empty container
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        # LIFO
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)
