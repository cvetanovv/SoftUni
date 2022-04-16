from project.astronaut import astronaut_repository
from project.planet import planet_repository


class SpaceStation:
    def __init__(self):
        self.planet_repository = planet_repository
        self.astronaut_repository = astronaut_repository