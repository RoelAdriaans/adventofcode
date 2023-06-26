from adventofcode2016.utils.node import Node


def test_node():
    n1 = Node("n1", None, cost=1, heuristic=0.5)
    n2 = Node("n2", None, cost=3, heuristic=0.5)

    # test __lt__ < and >
    assert n1 < n2
    assert n2 > n1

    assert not n1 > n2
    assert not n2 < n1
