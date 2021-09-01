import math

vineyard_meter = int(input())
grapes_for_one_meter = float(input())
needed_liters_wine = int(input())
workers_number = int(input())

total_grapes = vineyard_meter * grapes_for_one_meter
total_wine = (total_grapes * 0.40) / 2.5

if total_wine >= needed_liters_wine:
    left_wine = total_wine - needed_liters_wine
    wine_per_worker = left_wine / workers_number
    print(f"Good harvest this year! Total wine: {math.floor(total_wine)} liters.")
    print(f"{math.ceil(left_wine)} liters left -> {math.ceil(wine_per_worker)} liters per person.")
else:
    needed_wine = needed_liters_wine - total_wine
    print(f"It will be a tough winter! More {math.floor(needed_wine)} liters wine needed.")