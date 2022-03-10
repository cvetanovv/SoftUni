class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity <= len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salary = 0
        for w in self.workers:
            all_salary += w.salary
        if self.__budget >= all_salary:
            self.__budget -= all_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        all_animal_money_for_care = 0
        for a in self.animals:
            all_animal_money_for_care += a.money_for_care
        if self.__budget >= all_animal_money_for_care:
            self.__budget -= all_animal_money_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += lion.__repr__() + "\n"

        tigers = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += tiger.__repr__() + "\n"

        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Cheetah":
                cheetahs.append(animal)
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += cheetah.__repr__() + "\n"

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
        result += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result += keeper.__repr__() + "\n"

        caretakers = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Caretaker":
                caretakers.append(worker)
        result += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result += caretaker.__repr__() + "\n"

        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                vets.append(worker)
        result += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result += vet.__repr__() + "\n"
        return result.strip()