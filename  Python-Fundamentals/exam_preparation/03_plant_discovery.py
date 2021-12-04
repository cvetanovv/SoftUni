number_of_plants = int(input())
plants = {}

for _ in range(number_of_plants):
    input_plants = input().split("<->")
    plant = input_plants[0]
    plant_rarity = int(input_plants[1])
    plants[plant] = {"rarity": plant_rarity, "rating": 0.00}

command = input()

while command != "Exhibition":
    command = command.split(":")
    action = command[0]
    if action == "Rate":
        operation = command[1].strip().split(" - ")
        plant = operation[0]
        rating = int(operation[1])
        if plant in plants:
            plants[plant]["rating"] += rating
        else:
            print("error")
    elif action == "Update":
        operation = command[1].strip().split(" - ")
        plant = operation[0]
        new_rarity = int(operation[1])
        if plant in plants:
            plants[plant]["rarity"] = new_rarity
        else:
            print("error")
    elif action == "Reset":
        plant = command[1].strip()
        if plant in plants:
            plants[plant]["rating"] = 0.00
        else:
            print("error")
    command = input()

sorted_plants = sorted(plants.items(), key=lambda kvp: (-kvp[1]["rarity"], -kvp[1]["rating"]))

print("Plants for the exhibition:")
for plant, grades in sorted_plants:
    print(f"- {plant}; Rarity: {grades['rarity']}; Rating: {grades['rating']:.2f}")