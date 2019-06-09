import pprint


# filename = "test"
filename = "input"

# filename = "test2"
# answer should be: XIJACQ
# answer shouldn't be: XIJAQC

class Node(object):
    def __init__(self, name):
        self.name = name
        self.parents = {}
        self.childs = {}
        self.completed = False

    def __repr__(self):
        return "Node {} with parents {} -  Childs - {}".format(
            self.name,
            ", ".join(self.parents),
            ", ".join(self.childs),
        )

    def is_root_node(self):
        if len(self.parents) == 0:
            return True
        else:
            return False

    def _has_parent_fished(self):
        if self.is_root_node():
            # No parents, we are done
            return True
        is_finished = True
        for node in self.parents.itervalues():
            if not node.completed:
                is_finished = False
        return is_finished

    def work(self, finished):
        # We can only work if our parents are finished
        # If we are already finished, just return
        if self.completed:
            return finished

        if self._has_parent_fished():
            # We are done!
            self.completed = True
            finished = "{}{}".format(finished, self.name)
        # Do we have childeren:
        # for work_node in self.childs.itervalues():
        #     finished = work_node.work(finished)
        return finished


class Nodes(object):
    def __init__(self):
        self.nodes = {}

    def get_node(self, name):
        if name in self.nodes:
            return self.nodes[name]
        else:
            new_node = Node(name)
            self.nodes[name] = new_node
            return new_node

    def add_parent(self, child, parent):
        """ Add a parent to child """
        parent_node = self.get_node(parent)
        child_node = self.get_node(child)

        parent_node.childs[child] = child_node
        child_node.parents[parent] = parent_node

    def __repr__(self):
        x = "\n".join([value.__repr__() for value in self.nodes.iteritems()])
        return x

    def work(self):
        """ Work on all the steps"""
        root_nodes = [x for x in self.nodes.itervalues() if x.is_root_node()]
        print("We have {} root nodes: {}".format(len(root_nodes), root_nodes))

        finished = ""
        while len(finished) != len(self.nodes):
            # for work_node in root_nodes:
            #     finished = work_node.work(finished)
            for work_node in self.nodes.itervalues():
                new_finished = work_node.work(finished)
                if finished != new_finished:
                    # We changed something, restart
                    finished = new_finished
                    break

        return finished


if __name__ == "__main__":
    lines = open(filename, 'r').readlines()

    nodes = Nodes()

    for line in lines:
        words = line.split(' ')
        if len(words) <= 7:
            continue
        parent = words[1]
        name = words[7]

        # node = Node(name)
        # print node
        new_node = nodes.get_node(name)
        nodes.add_parent(child=name, parent=parent)

    pp = pprint.PrettyPrinter(indent=4)
    print(nodes)
    print("Resultaat:")
    print (nodes.work())


# FYDBRIPCOMTAJWQVHXNGZUEKLS
# FRYDBICOMTAJWPQVHXNGZUEKLS