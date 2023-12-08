from solutions.day12 import Day12PartA, Garden


class TestDay12PartA:
    test_input_string = "#..#.#..##......###...###"
    test_notes = """...## => #
    ..#.. => #
    .#... => #
    .#.#. => #
    .#.## => #
    .##.. => #
    .#### => #
    #.#.# => #
    #.### => #
    ##.#. => #
    ##.## => #
    ###.. => #
    ###.# => #
    ####. => #
    ..... => .
    """

    def test_day12a_grid(self):
        solution = Garden(list(self.test_input_string))
        solution.split_notes(self.test_notes.split("\n"))
        # Check that out string is parsed with some spares
        assert len(solution.table) == len(self.test_input_string) + solution.offset * 2

        # We should have all the combinations in there (5 spots, 2 options == 2*2*2*2*2)
        assert len(solution.notes) == 32

        # assert repr(solution) == "....." + self.test_input_string + "....."
        assert "...#..#.#..##......###...###.." in (repr(solution))  # Start (0)
        # assert solution.offset == 5
        assert solution.table[0 + solution.offset] == solution.PLANT
        assert solution.table[3 + solution.offset] == solution.PLANT
        # Do a generation
        solution.generate()
        assert "...#...#....#.....#..#..#..#.." in repr(solution)  # 1

        solution.generate()
        assert "...##..##...##....#..#..#..##." in repr(solution)  # 2

        solution.generate()
        # assert solution.offset == 1
        #       32101234567890
        assert solution.generation == 3
        assert "..#.#...#..#.#....#..#..#...#..." in repr(solution)  # 3
        assert solution.table[-1 + solution.offset] == solution.PLANT
        assert solution.table[0 + solution.offset] == solution.EMPTY
        assert solution.table[1 + solution.offset] == solution.PLANT

        solution.generate(4)
        assert solution.generation == 7
        assert "...#..###.#...##..#...#...#...#...." in repr(solution)  # 7

        solution.generate(10)
        assert solution.generation == 17
        assert "..#...##...#.#.#.#...##...#....#...#.." in repr(solution)  # 17

        solution.generate(3)
        assert solution.generation == 20
        assert ".#....##....#####...#######....#.#..##." in repr(solution)  # 20
        # assert solution.offset == 2
        assert solution.table[-2 + solution.offset] == solution.PLANT
        assert solution.table[34 + solution.offset] == solution.PLANT
        assert solution.table[33 + solution.offset] == solution.PLANT
        assert solution.table[32 + solution.offset] == solution.EMPTY

        assert solution.count_plants() == 325

    def test_day12a_solve(self):
        solution = Day12PartA()
        res = solution("day_12/day12_test.txt")
        assert res == 325

    def test_day12a_data(self):
        """Result we got when we did the real solution"""
        solution = Day12PartA()
        res = solution("day_12/day12.txt")
        assert res == 2911
