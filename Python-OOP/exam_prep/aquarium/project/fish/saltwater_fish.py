from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    INCREASE_FISH_SIZE = 2

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)