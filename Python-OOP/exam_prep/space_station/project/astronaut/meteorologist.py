from project.astronaut.astronaut import Astronaut


class Meteorologist (Astronaut):
    BREATH_DECREASE = 15

    def __init__(self, name: str):
        super().__init__(name, 90)