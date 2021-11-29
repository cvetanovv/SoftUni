number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    car_input = input().split("|")
    car = car_input[0]
    mileage = int(car_input[1])
    fuel = int(car_input[2])
    cars[car] = {"mileage": mileage, "fuel": fuel}

command = input()

while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["mileage"] += distance
            cars[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car]["mileage"] >= 100_000:
            print(f"Time to sell the {car}!")
            del cars[car]
    if action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        if cars[car]["fuel"] + fuel > 75:
            print(f"{car} refueled with {75 - cars[car]['fuel']} liters")
            cars[car]["fuel"] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
            cars[car]["fuel"] += fuel
    if action == "Revert":
        car = command[1]
        kilometers = int(command[2])
        if cars[car]["mileage"] - kilometers < 10_000:
            cars[car]["mileage"] = 10_000
        else:
            cars[car]["mileage"] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
    command = input()

sorted_cars = sorted(cars.items(), key=lambda kvp: (-kvp[1]["mileage"], kvp[0]))
for car, car_data in sorted_cars:
    print(f"{car} -> Mileage: {car_data['mileage']} kms, Fuel in the tank: {car_data['fuel']} lt.")