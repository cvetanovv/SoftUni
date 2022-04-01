class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)



from unittest import TestCase, main

class CarManagerTest(TestCase):
    def setUp(self) -> None:
        self.my_car = Car("Audi", "A4", 5, 20)

    def test_init_method(self):
        my_car = Car("Audi", "A4", 5, 20)
        self.assertEqual(my_car.make, "Audi")
        self.assertEqual(my_car.model, "A4")
        self.assertEqual(my_car.fuel_consumption, 5)
        self.assertEqual(my_car.fuel_capacity, 20)
        self.assertEqual(my_car.fuel_amount, 0)

    def test_make_is_not_null_or_empty_str(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_is_not_null_or_empty_str(self):
        with self.assertRaises(Exception) as ex:
            self.my_car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_cant_be_zero_or_negative(self):
        for consumption in [0, -10]:
            with self.assertRaises(Exception) as ex:
                my_car = Car("Audi", "A4", consumption, 20)
            self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_cant_be_zero_or_negative(self):
        for capacity in [0, -10]:
            with self.assertRaises(Exception) as ex:
                my_car = Car("Audi", "A4", 5, capacity)
            self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_cannot_be_negative(self):
        my_car = Car("Audi", "A4", 5, 20)
        with self.assertRaises(Exception) as ex:
            my_car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_or_negative(self):
        refuel_numbers = [0, -5]
        for refuel in refuel_numbers:
            with self.assertRaises(Exception) as ex:
                self.my_car.refuel(refuel)
            self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_amount_bigger_that_car_capacity(self):
        my_car = Car("Audi", "A4", 5, 20)
        my_car.refuel(5)
        self.assertEqual(5, my_car.fuel_amount)
        my_car.refuel(30)
        self.assertEqual(20, my_car.fuel_amount)

    def test_drive_method_working_properly(self):
        my_car = Car("Audi", "A4", 5, 20)
        my_car.refuel(20)
        my_car.drive(50)
        self.assertEqual(17.5, my_car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            my_car.drive(1000000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
