from unittest import TestCase
import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'



from unittest import TestCase, main

class WorkerTests(TestCase):

    def test_worker_is_initialized_correct(self):
        worker = Worker("Test", 1000, 100)

        self.assertEqual("Test", worker.name)
        self.assertEqual(1000, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_energy_incremented_after_rest(self):
        # Arrange
        worker = Worker("Test", 1000, 100)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(101, worker.energy)

    def test_if_error_raised_if_worker_work_with_negative_or_zero_energy(self):
        # Arrange
        worker = Worker("Test", 1000, 0)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_worker_money_increased_by_his_salary_correctly(self):
        # Arrange
        worker = Worker("Test", 1000, 100)

        # Act
        worker.work()

        # Assert
        self.assertEqual(1000, worker.money)

    def test_if_worker_energy_decreased_after_work(self):
        # Arrange
        worker = Worker("Test", 1000, 100)

        # Act
        worker.work()

        # Assert
        self.assertEqual(99, worker.energy)

    def test_get_info_method(self):
        # Arrange
        worker = Worker("Test", 1000, 100)

        # Act
        worker.get_info()

        # Assert
        self.assertEqual("Test has saved 0 money.", worker.get_info())


if __name__ == '__main__':
    main()
