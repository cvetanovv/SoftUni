from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("testname", 2)

    def test_train_init(self):
        name = "testname"
        capacity = 5
        train = Train(name, capacity)
        self.assertEqual(name, train.name)
        self.assertEqual(capacity, train.capacity)
        self.assertEqual([], train.passengers)

    def test_raise_value_error_for_adding_more_passenger(self):
        self.train.passengers = ["name1", "name2"]
        with self.assertRaises(Exception) as ex:
            self.train.add("Oscar")
        self.assertEqual("Train is full", str(ex.exception))

    def test_if_passenger_name_in_passengers(self):
        self.train.passengers = ["Oscar"]
        with self.assertRaises(Exception) as ex:
            self.train.add("Oscar")
        self.assertEqual("Passenger Oscar Exists", str(ex.exception))

    def test_add_passenger_without_problem(self):
        result = self.train.add("Oscar")
        self.assertTrue("Oscar" in self.train.passengers)
        self.assertEqual("Added passenger Oscar", result)

    def test_remove_not_exist_passenger(self):
        with self.assertRaises(Exception) as ex:
            self.train.remove("Ivan")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_passenger(self):
        self.train.passengers = ["Mario"]
        result = self.train.remove("Mario")
        self.assertTrue("Mario" not in self.train.passengers)
        self.assertEqual("Removed Mario", result)

if __name__ == '__main__':
    main()