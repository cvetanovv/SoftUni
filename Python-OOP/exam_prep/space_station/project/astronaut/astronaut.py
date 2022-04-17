from abc import ABC, abstractmethod


class Astronaut(ABC):
    BREATH_DECREASE = 10

    #@abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.BREATH_DECREASE

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def __repr__(self):
        result = f"Name: {self.name}" + '\n'
        result += f"Oxygen: {self.oxygen}" + '\n'
        result += f"Backpack items: {', '.join(self.backpack) if len(self.backpack) > 0 else 'none'}"
        return result