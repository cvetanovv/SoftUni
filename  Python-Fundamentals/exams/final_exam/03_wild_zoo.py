zoo = {}

command = input()

while command != "EndDay":
    command = command.split(":")
    action = command[0]
    operation = command[1].strip().split("-")
    if action == "Add":
        animal = operation[0]
        needed_food = int(operation[1])
        area = operation[2]
        if animal not in zoo:
            zoo[animal] = {"needed_food": needed_food, "area": area}
        else:
            zoo[animal]["needed_food"] += needed_food
    elif action == "Feed":
        animal = operation[0]
        food = int(operation[1])
        if animal in zoo:
            if zoo[animal]["needed_food"] - food <= 0:
                print(f"{animal} was successfully fed")
                del zoo[animal]
            else:
                zoo[animal]["needed_food"] -= food
    command = input()

sorted_animals = sorted(zoo.items(), key=lambda kvp: (-kvp[1]["needed_food"], kvp[0]))

print("Animals:")
for animal_name, characteristics in sorted_animals:
    print(f" {animal_name} -> {characteristics['needed_food']}g")

dic_of_areas = {}
for animal_name, characteristics in sorted_animals:
    area = characteristics["area"]
    if area not in dic_of_areas:
        dic_of_areas[area] = {"area": 1}
    else:
        dic_of_areas[area]["area"] += 1

sorted_areas = sorted(dic_of_areas.items(), key=lambda kvp: (-kvp[1]["area"], kvp[0]))
print("Areas with hungry animals:")
for area_name, number_of_hungry_animals in sorted_areas:
    print(f" {area_name}: {number_of_hungry_animals['area']}")