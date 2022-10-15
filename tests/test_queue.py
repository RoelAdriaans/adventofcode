import pytest

from adventofcode2021.utils.queue import Queue


def test_queue():
    q = Queue()

    assert q.empty
    assert q.__repr__() == "deque([])"

    # Let's add some stuff
    q.push("a")
    q.push("b")
    q.push("c")

    assert not q.empty
    assert len(q) == 3
    assert q.__repr__() == "deque(['a', 'b', 'c'])"

    # First in is First out
    assert q.pop() == "a"
    assert q.pop() == "b"
    assert q.pop() == "c"

    # And empty again
    assert q.empty
    assert len(q) == 0

    with pytest.raises(IndexError):
        q.pop()
