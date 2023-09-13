import unittest
import car, motorcycle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = car.Car()
        self.type_vehicle = car.Car
        self.vehicle_num_wheels = 4
        self.vehicle_speed_test_drive = 60
        self.vehicle_speed_park = 0

        # self.vehicle = motorcycle.Motorcycle()
        # self.type_vehicle = motorcycle.Motorcycle
        # self.vehicle_num_wheels = 2
        # self.vehicle_speed_test_drive = 75

    def test_vehicle_type(self):
        self.assertTrue(isinstance(self.vehicle, self.type_vehicle)), "не является экземпляром класса"

    def test_vehicle_num_wheels(self):
        self.assertEqual(self.vehicle.num_wheels, self.vehicle_num_wheels), f"несоответствие количества колес"

    def test_vehicle_test_drive(self):
        self.assertEqual(self.vehicle.test_drive(),
                         self.vehicle_speed_test_drive), f"не соответствие скорости"

    def test_vehicle_park(self):
        self.vehicle.test_drive()
        self.vehicle.park()
        self.assertEqual(self.vehicle.speed,
                         self.vehicle_speed_park), f"скорость после парковки должна равняться 0"


if __name__ == '__main__':
    unittest.main()
