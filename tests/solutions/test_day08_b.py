from adventofcode2016.solutions.day08 import Day08PartB


class TestDay08PartB:
    def test_day08b_data(self):
        """Result we got when we did the real solution"""
        solution = Day08PartB()
        res = solution("day_08/day08.txt")
        expected = [
            "████ ████ ████ █   ██  █ ████ ███  ████  ███   ██ ",
            "█    █    █    █   ██ █  █    █  █ █      █     █ ",
            "███  ███  ███   █ █ ██   ███  █  █ ███    █     █ ",
            "█    █    █      █  █ █  █    ███  █      █     █ ",
            "█    █    █      █  █ █  █    █ █  █      █  █  █ ",
            "████ █    ████   █  █  █ █    █  █ █     ███  ██  ",
        ]
        assert res == "\n".join(expected)
