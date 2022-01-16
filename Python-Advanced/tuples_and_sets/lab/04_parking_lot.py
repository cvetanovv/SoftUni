n = int(input())

parking = set()

for _ in range(n):
    action, car_number = input().split(", ")
    if action == "IN":
        parking.add(car_number)
    else:
        parking.discard(car_number)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")