from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.myshop = PetShop("Petshop")

    def test_init_method(self):
        name = "Petshop"

        petshop = PetShop(name)

        self.assertEqual(petshop.name, "Petshop")
        self.assertEqual(petshop.food, {})
        self.assertEqual(petshop.pets, [])

    def test_add_food_with_zero_or_less_quantity(self):
        values = [0 , -10]
        for value in values:
            with self.assertRaises(Exception) as ex:
                self.myshop.add_food("bread", value)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_successfully_added_food(self):
        result = self.myshop.add_food("bread", 10)
        self.assertEqual(f"Successfully added {10:.2f} grams of bread.", result)

    def test_successfully_added_pet(self):
        result = self.myshop.add_pet("Oscar")
        self.assertEqual(f"Successfully added Oscar.", result)

    def test_add_pet_with_same_name(self):
        self.myshop.add_pet("Oscar")
        with self.assertRaises(Exception) as ex:
            self.myshop.add_pet("Oscar")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_with_invalid_name(self):
        with self.assertRaises(Exception) as ex:
            self.myshop.feed_pet("bread", "invalid_name")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_if_food_name_not_exist(self):
        self.myshop.add_pet("Oscar")
        result = self.myshop.feed_pet("salami", "Oscar")
        self.assertEqual(f'You do not have salami', result)

    def test_food_is_less_that_100(self):
        self.myshop.add_pet("Oscar")
        self.myshop.add_food("bread", 50)
        result = self.myshop.feed_pet("bread", "Oscar")
        self.assertEqual("Adding food...", result)

    def test_pet_is_successfully_fed(self):
        self.myshop.add_pet("Oscar")
        self.myshop.add_food("bread", 101)
        result = self.myshop.feed_pet("bread", "Oscar")
        self.assertEqual(f"Oscar was successfully fed", result)

    def test_repr_method(self):
        best_shop = PetShop("Best")
        best_shop.add_pet("Oscar")
        result = f'Shop {best_shop.name}:\n' \
               f'Pets: {", ".join(best_shop.pets)}'
        expected_result = f'Shop Best:\n' \
               f'Pets: Oscar'
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
