from adventofcode.utils.abstract import FileReaderSolution


class Node:
    metadata: list = None
    children: list = None

    def __init__(self, metadata=False):
        self.children = []
        if not metadata:
            self.metadata = list()
        else:
            self.metadata = metadata

    def add_child(self, child: Node):
        self.children.append(child)

    def value(self):
        """Compute the value of this node, and it's children"""
        if len(self.children) == 0:
            return sum(self.metadata)
        # We have to go for the indexing method:
        count = 0
        for meta_entry in self.metadata:
            try:
                count += self.children[meta_entry - 1].value()
            except IndexError:
                pass
        return count


class Day08:
    def __init__(self):
        self.nodes = list()

    def parse_data(self, input_data: str) -> [int]:
        """Parse a string of numbers seperated by spaces, and return a list of ints"""
        return [int(numb) for numb in input_data.split(" ")]

    def create_nodes(
        self, numbers: [int], read_position=0, parent_node: Node = False
    ) -> int:
        qty_child_nodes = numbers[read_position]
        read_position += 1
        qty_meta_data = numbers[read_position]
        read_position += 1

        new_node = Node()
        if parent_node:
            parent_node.add_child(new_node)
        # Go look at child nodes.
        for _ in range(qty_child_nodes):
            read_position = self.create_nodes(numbers, read_position, new_node)

        metadata = numbers[read_position : read_position + qty_meta_data]
        new_node.metadata = metadata
        self.nodes.append(new_node)

        new_position = read_position + qty_meta_data
        return new_position

    def compute_sum_metadata(self) -> int:
        """Create the sum of all the nodes"""
        checksum = [node.metadata for node in self.nodes]
        res = sum(list(map(sum, checksum)))
        return res


class Day08PartA(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        numbers = self.parse_data(input_data)
        self.create_nodes(numbers)
        result = self.compute_sum_metadata()
        return result


class Day08PartB(Day08, FileReaderSolution):
    def solve(self, input_data: str) -> int:
        numbers = self.parse_data(input_data)
        self.create_nodes(numbers)
        root_node = self.nodes[-1]
        res = root_node.value()
        return res
