import pytest

from adventofcodeutils.priority_queue import PriorityQueue


def test_priorityqueue():
    q = PriorityQueue()

    assert q.empty
    assert q.__repr__() == "[]"

    # Let's add some stuff. The priority is not in order.
    q.push((1, "a"))
    q.push((3, "c"))
    q.push((2, "b"))

    assert not q.empty
    assert len(q) == 3
    # Repr is based on the insert order (?)
    assert q.__repr__() == "[(1, 'a'), (3, 'c'), (2, 'b')]"

    # Output is based on the priority
    assert q.pop() == (1, "a")
    assert q.pop() == (2, "b")
    assert q.pop() == (3, "c")

    # And empty again
    assert q.empty
    assert len(q) == 0

    with pytest.raises(IndexError):
        q.pop()
