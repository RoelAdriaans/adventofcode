import pytest

from adventofcode2021.solutions.day16 import Day16PartA, Packet


class TestDay16PartA:
    def test_packet_parsing(self):
        test_data = "D2FE28"
        packet = Packet(test_data)
        assert packet.version == 6
        assert packet.type_id == 4
        assert packet.value == 2021

        # We still have 3 unused bits over
        assert len(packet.packet_str) == 3

    def test_packet_operator(self):
        test_data = "38006F45291200"
        packet = Packet(test_data)
        assert packet.version == 1
        assert packet.type_id == 6

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    @pytest.mark.parametrize(("input_data", "expected_result"), [("", ""), ("", "")])
    def test_day16a_solve(self, input_data, expected_result):
        solution = Day16PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    @pytest.mark.xfail(reason="Not yet implemented", raises=NotImplementedError)
    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 0
