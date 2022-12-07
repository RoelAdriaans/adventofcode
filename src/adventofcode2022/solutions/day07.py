from __future__ import annotations

import logging
from collections import Counter
from enum import Enum

from adventofcode2022.utils.abstract import FileReaderSolution

logger = logging.getLogger(__name__)


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
            return sum(item.total_size() for item in self.contains)


class Day07:
    def parse_input(self, input_data: str) -> Node:
        """Parse the input data and return the root node"""
        root_node = Node(name="/", node_type=Type.root)
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
    @staticmethod
    def calculate_directory_size(root_node) -> int:
        to_check: list[Node] = [root_node]
        total = 0
        while to_check:
            node = to_check.pop()
            logger.info(f"Checking node {node.name}")
            for child in node.contains:
                if child.node_type == Type.directory:
                    to_check.append(child)

            if node.total_size() <= 100000:
                total += node.total_size()

        return total

    def solve(self, input_data: str) -> int:
        logger.info("Start parsing")
        root_node = self.parse_input(input_data)
        logger.info("Parsing done")

        return self.calculate_directory_size(root_node)


class Day07PartB(Day07, FileReaderSolution):
    def calculate_directory_sizes(self, root_node:Node)->dict[str, int]:
        to_check: list[Node] = [root_node]
        dir_sizes = {}

        while to_check:
            node = to_check.pop()
            logger.info(f"Checking node {node.name}")
            for child in node.contains:
                if child.node_type == Type.directory:
                    to_check.append(child)
            dir_sizes[node.name] = node.total_size()

        return dir_sizes


    def solve(self, input_data: str) -> int:
        logger.info("Start parsing")
        root_node = self.parse_input(input_data)
        logger.info("Parsing done")

        sizes = self.calculate_directory_sizes(root_node)
        sorted_sizes = dict(sorted(sizes.items(), key=lambda item: item[1]))
        total_size = 70_000_000
        required_free_space = 30_000_000
        total_used = sizes["/"]
        unused = total_size - total_used
        # We have `unused` unused free space, we need required_free_space;
        still_required = required_free_space - unused
        for name, size in sorted_sizes.items():
            if size > still_required:
                return size
        return -1