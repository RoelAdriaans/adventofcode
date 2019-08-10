from utils.abstract import FileReaderSolution
import re


class TimedNode:
    name = None
    seconds_worked_on = 0
    seconds_to_work = 0

    def __init__(self, name, extra_seconds=0):
        self.name = name
        # Compute home many seconds we have left
        self.seconds_to_work = ord(name) - ord("A") + extra_seconds + 1

    def is_complete(self):
        return self.seconds_to_work <= self.seconds_worked_on

    def work(self):
        if self.time_left() > 0:
            self.seconds_worked_on += 1

    def time_left(self) -> int:
        return self.seconds_to_work - self.seconds_worked_on

    def __repr__(self):
        return f"{self.name} ({self.seconds_to_work} - {self.seconds_worked_on})"


class Day07:
    def __init__(self):
        self.node_tree = dict()
        self.walked_nodes = list()
        self.nodes_worked_on = list()

    @staticmethod
    def parse_string(input_string: str) -> (str, str):
        """
        Parse a string and return the in and out nodes.
        Example input:
        "Step C must be finished before step A can begin.",

        Returns:
        (C, A)

        """
        regex = (
            "Step (?P<before>[A-Z]) must be finished before step "
            "(?P<after>[A-Z]) can begin."
        )
        matches = re.match(regex, input_string)
        return matches["before"], matches["after"]

    @staticmethod
    def parse_strings(input_strings) -> [tuple]:
        """ Parse strings into tuples"""
        return [Day07.parse_string(line) for line in input_strings]

    def build_tree(self, nodes: [tuple]):
        """ Build a tree of the nodes in `nodes`.
        Nodes is a tuple in the pair (Before, After)
        """
        for node in nodes:
            if node[0] in self.node_tree:
                self.node_tree[node[0]].append(node[1])
            else:
                self.node_tree[node[0]] = [node[1]]
            # Also add the children as Nodes.
            if node[1] not in self.node_tree:
                self.node_tree[node[1]] = list()

    def get_parent(self, child: str) -> [str]:
        """ Return the parent(s) of this child as a list"""
        parents = []
        for node, children in self.node_tree.items():
            if child in children:
                parents.append(node)

        return sorted(parents)

    def validate_node_ready(self, search_node: str):
        """ Validate if we can visit this node. This is true when the parent of
        this node is in visited_node
        """
        for node, children in self.node_tree.items():
            if search_node in children:
                # We have a parent!
                if node not in self.walked_nodes:
                    # Our parent hasn't been visited yet.
                    return False
        return True

    def walk_tree(self, root_node):
        """ Walk the tree, and see the order"""
        # First we have to add the starting node to our result, and visited list
        self.walked_nodes = list()
        self.walked_nodes.append(root_node)
        while len(self.walked_nodes) < len(self.node_tree):
            # For a node to be ready, the parent needs to be in visited_nodes
            next_node = self.get_next_node()
            self.walked_nodes.append(next_node)

        return "".join(self.walked_nodes)

    def get_next_node(self):
        valid_nodes = list()
        for node in self.node_tree.keys():
            if (
                node not in self.walked_nodes
                and node not in self.nodes_worked_on
                and self.validate_node_ready(node)
            ):
                valid_nodes.append(node)
        if valid_nodes:
            valid_nodes = sorted(valid_nodes)
            next_node = valid_nodes[0]
            return next_node
        else:
            return False

    def get_root(self) -> str:
        """ Get the root node and return this as String.

        The root is defined as a key without parents.
        If there are multiple parents, sort them.
        """
        nodes_with_parents = list(self.node_tree.keys())
        for node, children in self.node_tree.items():
            for child in children:
                if child in nodes_with_parents:
                    nodes_with_parents.remove(child)
        return sorted(nodes_with_parents)[0]

    def walk_tree_with_helpers(self, extra_time: int = 60, num_workers: int = 5) -> int:
        """
        Walk the tree, but we now have helpers!
        """
        current_second = 0
        work_nodes = {
            name: TimedNode(name, extra_time) for name in self.node_tree.keys()
        }
        # We start at second 0.
        # The first worker will start on the root_node
        workers = [False for _ in range(num_workers)]

        while len(self.walked_nodes) < len(self.node_tree):
            self.nodes_worked_on = [x.name for x in workers if x]
            for idx, worker in enumerate(workers):
                # Loop over the workers, and let them work!
                if worker:
                    worker.work()
                    if worker.is_complete():
                        self.walked_nodes.append(worker.name)
                        workers[idx] = False
            # All our workers have worked, or not. Let's see if there are any free
            # workers.
            for idx, worker in enumerate(workers):
                # Check if we have a node we can assign to this worker:
                free_node = self.get_next_node()
                if free_node:
                    workers[idx] = work_nodes[free_node]
                    self.nodes_worked_on = [x.name for x in workers if x]

            current_second += 1
        return current_second - 1


class Day07PartA(Day07, FileReaderSolution):
    def solve(self, input_data: str) -> str:
        input_lines = input_data.strip().split("\n")
        nodes = self.parse_strings(input_lines)
        self.build_tree(nodes)
        root_node = self.get_root()
        result = self.walk_tree(root_node)
        return result


class Day07PartB(Day07, FileReaderSolution):
    def solve(self, input_data: str, extra_time: int = 60, num_workers: int = 5) -> int:
        input_lines = input_data.strip().split("\n")
        nodes = self.parse_strings(input_lines)
        self.build_tree(nodes)
        result = self.walk_tree_with_helpers(
            extra_time=extra_time, num_workers=num_workers
        )
        return result
