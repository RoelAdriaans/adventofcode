from __future__ import annotations

from enum import Enum

from adventofcode2022.utils.abstract import FileReaderSolution


class Type(str, Enum):
    root = "root"
    file = "file"
    directory = "directory"


class Node:
    name: str
    node_type: Type
    size: int | None
    contains: list[Node]
    parent: Node | None

    def __init__(self, name, node_type: Type, size=0, parent=None):
        self.name = name
        self.node_type = node_type
        self.size = size
        self.contains = []
        self.parent = parent

    def __repr__(self):
        return (
            f"Node-{self.node_type}({self.name}, {self.size=}, "
            f"Content: {';'.join(repr(child) for child in self.contains)})"
        )

    def add_subdirectory(self, name) -> Node:
        """Create a new subdirectory, add it to the list of folders and return it"""
        new_dir = Node(name=name, node_type=Type.directory, parent=self)
        self.contains.append(new_dir)

        return new_dir

    def add_file(self, name: str, size: int) -> Node:
        """Create a new file in this subdirectory"""
        new_file = Node(name=name, node_type=Type.file, size=size, parent=self)
        self.contains.append(new_file)
        return new_file

    def find_subdirectory(self, name) -> Node:
        """Find a subdirectory in this node"""
        for node in self.contains:
            if node.name == name and node.node_type == Type.directory:
                return node
        raise KeyError("%s not found!", name)

    def total_size(self) -> int:
        if self.node_type == Type.file:
            return self.size
        else:
            return sum(item.size for item in self.contains)


class Day07:
    def parse_input(self, input_data: str) -> Node:
        """Parse the input data and return the root node"""
        root_node = Node(name="root", node_type=Type.root)
        current_folder = root_node
        for line in input_data.splitlines():
            parts = line.split()

            if line == "$ cd /":
                current_folder = root_node
            elif parts[0] == "$" and parts[1] == "cd" and parts[2] != "..":
                # Going into a directory
                current_folder = current_folder.find_subdirectory(parts[2])
            elif parts[0] == "$" and parts[1] == "cd" and parts[2] == "..":
                # Going up
                current_folder = current_folder.parent
            elif parts[0] == "$" and parts[1] == "ls":
                continue
            elif parts[0] == "dir":
                current_folder.add_subdirectory(parts[1])
            else:
                # This must be a file
                current_folder.add_file(name=parts[1], size=int(parts[0]))

        return root_node


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        root_node = self.parse_input(input_data)
        return -1


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        raise NotImplementedError
