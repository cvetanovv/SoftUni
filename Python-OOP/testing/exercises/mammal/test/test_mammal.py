from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Oscar", "Dog", "woof")

    def test_mammal_init(self):
        name = "Oscar"
        mammal_type = "Dog"
        sound = "woof"
        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(mammal.name, name)
        self.assertEqual(mammal.type, mammal_type)
        self.assertEqual(mammal.sound, sound)
        self.assertEqual(mammal._Mammal__kingdom, "animals")

    def test_make_sound_method(self):
        expected_result = f"{self.mammal.name} makes {self.mammal.sound}"
        result = self.mammal.make_sound()
        self.assertEqual(expected_result, result)

    def test_get_kingdom_method(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info_method(self):
        expected_result = f"{self.mammal.name} is of type {self.mammal.type}"
        result = self.mammal.info()
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()