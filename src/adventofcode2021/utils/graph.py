from collections import defaultdict
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Generic, TypeVar

# The type of the nodes
V = TypeVar("V")


@dataclass
class Edge(Generic[V]):
    u: V
    v: V

    def __repr__(self) -> str:
        return f"{self.u} -> {self.v}"

    def __hash__(self):
        return hash((self.u, self.v))


class Graph(Generic[V]):
    """
    Very simple graph, enough for advent of code.

    Definitions, that I always forget:
    - Nodes: The Vertices / items that are there
    - Edges: The links between vertices

    """

    def __init__(self, edges: Iterator[tuple[V, V]] = None):
        """Create a new graph.

        If edges is given, the network is created based on the edges.
        For example

        >>> g = Graph([("a", "b"), ("b", "c"), ("c", "a")])

        Will create simple Graph with:
        a <-> b
        b <-> c
        c <-> a
        """

        self._nodes: set[V] = set()
        self._edges: defaultdict[V, list[Edge]] = defaultdict(list)
        if edges:
            self.add_from_list(edges)

    def add_node(self, node: V):
        self._nodes.add(node)

    def add_edge(self, u: V, v: V):
        self.add_node(u)
        self.add_node(v)
        new_edge = Edge(u, v)
        self._edges[u].append(new_edge)
        self._edges[v].append(new_edge)

    def add_from_list(self, edges: Iterator[tuple[V, V]]):
        """Add edges based on a list"""
        for edge in edges:
            self.add_edge(*edge)

    def __repr__(self) -> str:
        return f"Graph with {len(self.nodes)} nodes and {len(self.edges)} edges"

    @property
    def edges(self) -> set[Edge]:
        """Return all the unique edges"""
        return {item for sublist in self._edges.values() for item in sublist}

    @property
    def nodes(self) -> set[V]:
        """Return all the nodes"""
        return self._nodes

    def edges_from_node(self, node: V) -> list[Edge]:
        """Return all the edges directly connected to node"""
        return self._edges[node]

    def nodes_from_node(self, node: V) -> Iterator[V]:
        """Return all the nodes directly connected to node"""
        for edge in self._edges[node]:
            if edge.v == node:
                yield edge.u
            else:
                yield edge.v
