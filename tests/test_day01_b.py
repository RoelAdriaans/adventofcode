from solutions.day01 import Day1PartB


class TestDay01PartB:
    def test_day01(self):
        d1 = Day1PartB()
        res = d1.solve("Appelflap")
        assert "Het result van b is: appelflap" == res
