class Weapon:
    def __init__(self, bullets):
        self.bullets = bullets
        self.__bullets = self.bullets

    def shoot(self):
        if self.__bullets > 0:
            self.__bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.__bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
