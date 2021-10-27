class Zoo:

    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal):
        if species == "mammal":
            self.mammals.append(animal)
        elif species == "fish":
            self.fishes.append(animal)
        elif species == "bird":
            self.birds.append(animal)
        self.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"

        result += f"Total animals: {self.__animals}"
        return result


zoo_name = input()
number_of_animals = int(input())

my_zoo = Zoo(zoo_name)

for i in range(number_of_animals):
    species, animal = input().split()
    my_zoo.add_animal(species, animal)

spices_to_print = input()

print(my_zoo.get_info(spices_to_print))