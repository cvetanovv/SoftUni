cities = {}

city_info = input()
while city_info != "Sail":
    city, population, gold = city_info.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    city_info = input()

command = input()
while command != "End":
    command = command.split("=>")
    event = command[0]
    if event == "Plunder":
        town, people, gold = command[1:]
        people = int(people)
        gold = int(gold)
        if cities[town]["population"] - people <= 0 or cities[town]["gold"] - gold <= 0:
            del cities[town]
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            print(f"{town} has been wiped off the map!")
        else:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            cities[town]["population"] -= people
            cities[town]["gold"] -= gold
    elif event == "Prosper":
        town = command[1]
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            command = input()
            continue
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")
    command = input()

print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
sorted_cities = sorted(cities.items(), key=lambda kvp: (-kvp[1]["gold"], kvp[0]))
a = 5
for city in sorted_cities:
    if cities:
        print(f"{city[0]} -> Population: {city[1]['population']} citizens, Gold: {city[1]['gold']} kg")
    else:
        print(f"Ahoy, Captain! All targets have been plundered and destroyed!")