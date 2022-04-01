from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Rens", 20, 50, 10)
        self.enemy = Hero("Mons", 15, 40, 5)

    def test_hero_init(self):
        username = "Rens"
        level = 20
        health = 50
        damage = 10

        hero = Hero(username, level, health, damage)

        self.assertEqual(hero.username, "Rens")
        self.assertEqual(hero.level, 20)
        self.assertEqual(hero.health, 50)
        self.assertEqual(hero.damage, 10)

    def test_if_hero_and_enemy_same_name(self):
        enemy = Hero("Rens", 15, 40, 5)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_hero_heath_is_zero_or_lower(self):
        for health in [0, -10]:
            self.hero = Hero("Rens", 20, health, 10)
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_heath_is_zero_or_lower(self):
        for health in [0, -10]:
            self.enemy = Hero("Mons", 15, health, 5)
            with self.assertRaises(ValueError) as ex:
                self.hero.battle(self.enemy)
            self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_if_both_heroes_is_zero_health_after_battle(self):
        self.hero = Hero("Rens", 20, 5, 10)
        self.enemy = Hero("Mons", 15, 10, 5)

        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_if_both_heroes_is_below_zero_health_after_battle(self):
        self.hero = Hero("Rens", 20, 1, 10)
        self.enemy = Hero("Mons", 15, 1, 5)

        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_if_hero_win(self):
        hero = Hero("Rens", 20, 50, 10)
        enemy = Hero("Mons", 15, 5, 2)

        result = hero.battle(enemy)
        self.assertEqual("You win", result)
        self.assertEqual(21, hero.level)
        self.assertEqual(25, hero.health)
        self.assertEqual(15, hero.damage)

    def test_if_enemy_win(self):
        hero = Hero("Rens", 15, 5, 2)
        enemy = Hero("Mons", 20, 50, 10)

        result = hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(21, enemy.level)
        self.assertEqual(25, enemy.health)
        self.assertEqual(15, enemy.damage)

    def test_string_repr_method(self):
        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        expected_result = f"Hero Rens: 20 lvl\n" \
               f"Health: 50\n" \
               f"Damage: 10\n"

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()