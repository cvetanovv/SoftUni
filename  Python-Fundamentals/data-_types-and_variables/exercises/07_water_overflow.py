number_of_iterations = int(input())
maximum_water_tank_capacity = 255
water_tank = 0

for _ in range(number_of_iterations):
    liters_of_water = int(input())
    water_tank += liters_of_water
    if water_tank > maximum_water_tank_capacity:
        water_tank -= liters_of_water
        print("Insufficient capacity!")
print(water_tank)