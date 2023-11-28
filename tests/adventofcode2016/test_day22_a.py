from adventofcode2016.day22 import Day22PartA, Node


class TestDay22PartA:
    def test_node(self):
        line = "/dev/grid/node-x0-y7     88T   68T    20T   77%"
        node = Node.from_string(line)
        assert node.x == 0
        assert node.y == 7
        assert node.size == 88
        assert node.used == 68
        assert node.avail == 20

    def test_day22a_data(self):
        """Result we got when we did the real solution"""
        solution = Day22PartA()
        res = solution("day_22/day22.txt")
        assert res == 952
