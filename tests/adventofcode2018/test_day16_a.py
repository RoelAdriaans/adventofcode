from adventofcode2018.day16 import Addi, Banr, Bori, Day16PartA, Device, Seti


class TestDay16PartA:
    def test_day16a_device_eq(self):
        device1 = Device()
        device2 = Device()

        assert device1 == device2

        device1.register[0] = 5

        assert device1 != device2

    def test_day16a_addi(self):
        # Add value from register A (0) and value 7 and store in register C (3)
        device = Device()
        Addi.execute(device, 0, 7, 3)
        assert device.register[0] == 0
        assert device.register[1] == 0
        assert device.register[2] == 0
        assert device.register[3] == 7

        # Add value from register A (3) and value 7 and store in register C (3)
        Addi.execute(device, 3, 3, 3)
        assert device.register[0] == 0
        assert device.register[1] == 0
        assert device.register[2] == 0
        assert device.register[3] == 10

    def test_day16a_banr_bori(self):
        # stores into register C the result of the bitwise AND of register A and
        # register B.
        device = Device()
        Seti.execute(device, 0xAA, None, 0)  # 1111 1100
        Seti.execute(device, 0xFC, None, 1)  # 1111 1100

        Banr.execute(device, 0, 1, 2)

        assert device.register[2] == 0xA8  # 1111 1000

        Bori.execute(device, 0, 0xFC, 3)
        assert device.register[3] == 0xFE  # 1111 1110

    def test_day16a_solve(self):
        input_data = "\n".join(
            ["Before: [3, 2, 1, 1]", "9 2 1 2", "After:  [3, 2, 2, 1]"]
        )
        expected_result = 1
        solution = Day16PartA()
        result = solution.solve(input_data)
        assert result == expected_result

    def test_day16a_data(self):
        """Result we got when we did the real solution"""
        solution = Day16PartA()
        res = solution("day_16/day16.txt")
        assert res == 618
