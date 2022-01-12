from collections import deque

quantity_of_water = int(input())
names = deque()

name = input()
while name != "Start":
    names.append(name)
    name = input()

command = input()
while command != "End":
    if command.isdigit():
        first_person = names.popleft()
        liters = int(command)
        if quantity_of_water >= liters:
            quantity_of_water -= liters
            print(f"{first_person} got water")
        else:
            print(f"{first_person} must wait")
    else:
        _, liters = command.split()
        liters = int(liters)
        quantity_of_water += liters

    command = input()

print(f"{quantity_of_water} liters left")