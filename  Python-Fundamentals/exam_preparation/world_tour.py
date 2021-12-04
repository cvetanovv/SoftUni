countries = input()

command = input()

while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index = int(command[1])
        country = command[2]
        if index < len(countries):
            countries = countries[:index] + country + countries[index:]
        print(countries)
    elif action == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < len(countries) and end_index < len(countries):
            countries = countries[0:start_index] + countries[end_index + 1:]
        print(countries)
    elif action == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in countries:
            countries = countries.replace(old_string, new_string)
        print(countries)
    command = input()

print(f"Ready for world tour! Planned stops: {countries}")
