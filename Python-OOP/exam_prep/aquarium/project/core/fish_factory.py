from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class FishFactory:
    fish_types = {
        "FreshwaterFish": FreshwaterFish,
        "SaltwaterFish": SaltwaterFish
    }

    def create_fish(self, fish_type, fish_name, species, price):
        if fish_type not in self.fish_types:
            raise ValueError(f"There isn't a fish of type {fish_type}.")
        return self.fish_types[fish_type](fish_name, species, price)
