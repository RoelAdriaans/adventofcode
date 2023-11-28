import pytest

from adventofcode2021.day16 import Day16PartA, Packet


class TestDay16PartA:
    def test_packet_parsing(self):
        test_data = "D2FE28"
        packet = Packet().from_hex(test_data)
        assert packet.version == 6
        assert packet.type_id == 4
        assert packet.value == 2021

        # We still have 3 unused bits over
        assert len(packet.packet_deq) == 3

    def test_packet_operator_zero(self):
        test_data = "38006F45291200"
        packet = Packet().from_hex(test_data)
        assert packet.version == 1
        assert packet.type_id == 6
        assert packet.length_type_id == 0
        assert len(packet.sub) == 2
        assert packet.sub[0].value == 10
        assert packet.sub[1].value == 20

    def test_packet_operator_one(self):
        test_data = "EE00D40C823060"
        packet = Packet().from_hex(test_data)
        assert packet.version == 7
        assert packet.type_id == 3
        assert packet.length_type_id == 1
        assert len(packet.sub) == 3
        assert packet.sub[0].value == 1
        assert packet.sub[1].value == 2
        assert packet.sub[2].value == 3

    def test_nested(self):
        packet = Packet().from_hex("8A004A801A8002F478")
        assert packet.version == 4
        assert len(packet.sub) == 1
        assert packet.sub[0].version == 1
        assert packet.sub[0].sub[0].version == 5
        assert packet.sub[0].sub[0].sub[0].version == 6

    @pytest.mark.parametrize(
        ("input_data", "expected_result"),
        [
            ("8A004A801A8002F478", 16),
            ("620080001611562C8802118E34", 12),
            ("C0015000016115A2E0802F182340", 23),
            ("A0016C880162017C3686B18A3D4780", 31),
        ],
    )
    def test_day16a_solve(self, input_data, expected_result):
        solution = Day16PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 981
