from adventofcode2016.utils.graph import Edge, Graph


def test_graph():
    """Test the graph"""
    g = Graph()
    g.add_from_list(
        [
            ("a", "b"),
            ("b", "c"),
            ("a", "d"),
        ]
    )
    assert repr(g) == "Graph with 4 nodes and 3 edges"
    assert g.nodes == {"a", "b", "c", "d"}
    assert Edge("a", "b") in list(g.edges)

    # Test the nodes reachable. From "a", we can connect to "b" and "d"
    assert g.edges_from_node("a") == [Edge("a", "b"), Edge("a", "d")]
    assert list(g.nodes_from_node("a")) == ["b", "d"]
