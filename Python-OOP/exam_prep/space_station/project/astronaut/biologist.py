from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATH_DECREASE = 5

    def __init__(self, name: str):
        super().__init__(name, 70)