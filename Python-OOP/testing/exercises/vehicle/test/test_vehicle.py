from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(90, 150)

    def test_vehicle_init(self):
        vehicle = Vehicle(90, 150)

        self.assertEqual(vehicle.fuel, 90)
        self.assertEqual(vehicle.horse_power, 150)
        self.assertEqual(vehicle.capacity, 90)
        self.assertEqual(vehicle.fuel_consumption, 1.25)

    def test_not_enough_fuel_for_drive(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_enough_fuel_for_drive(self):
        self.vehicle.drive(20)
        self.assertEqual(65.0, self.vehicle.fuel)

    def test_if_to_much_fuel(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_if_is_enough_fuel(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(10)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_string_method(self):
        result = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(self.vehicle.__str__(), result)

if __name__ == '__main__':
    main()