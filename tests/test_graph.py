from adventofcode2021.utils.graph import Graph, Edge


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
    assert list(g.edges)[0] == Edge("a", "b")
