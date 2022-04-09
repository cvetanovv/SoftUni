from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    @property
    def fish_type(self):
        return "SaltwaterFish"

    def __init__(self, name: str):
        super().__init__(name, 25)