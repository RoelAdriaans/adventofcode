from adventofcode2021.day11 import Day11PartA, Octopus


class TestDay11PartA:
    def test_octopus(self):
        squidward = Octopus(8)
        assert squidward.value == 8

        flashed = squidward.update()
        assert flashed is False
        assert squidward.value == 9

        flashed = squidward.update()
        assert flashed is True
        assert squidward.value == 0

    def test_simple(self):
        start_condition = """11111
19991
19191
19991
11111"""

        step_1 = """34543
40004
50005
40004
34543"""

        step_2 = """45654
51115
61116
51115
45654"""

        solution = Day11PartA()
        solution.create_grid(start_condition.splitlines())

        # Test that our print_grid() function works
        assert solution.print_grid() == start_condition

        # And step and validate
        solution.step()
        assert solution.print_grid() == step_1

        # And step and validate
        solution.step()
        assert solution.print_grid() == step_2

    def test_day11a_solve(self):
        start_condition = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
        step_1 = """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637"""
        step_2 = """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848"""
        step_3 = """0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000"""
        step_4 = """2263031977
0923031697
0032221150
0041111163
0076191174
0053411122
0042361120
5532241122
1532247211
1132230211"""
        solution = Day11PartA()
        solution.create_grid(start_condition.splitlines())

        # Test that our print_grid() function works
        assert solution.print_grid() == start_condition
        assert solution.total_flashes == 0
        # And step and validate
        solution.step()
        assert solution.print_grid() == step_1
        solution.step()
        assert solution.print_grid() == step_2
        solution.step()
        assert solution.print_grid() == step_3
        solution.step()
        assert solution.print_grid() == step_4

        # We have done 4 steps, let's do 6 more to reach the 10 steps
        for _ in range(0, 6):
            solution.step()
        assert solution.total_steps == 10
        assert solution.total_flashes == 204

        # And 100 steps
        for _ in range(0, 90):
            solution.step()
        assert solution.total_steps == 100
        assert solution.total_flashes == 1656

    def test_day11a_data(self):
        """Result we got when we did the real solution"""
        solution = Day11PartA()
        res = solution("day_11/day11.txt")
        assert solution.total_steps == 100
        assert res == 1601
