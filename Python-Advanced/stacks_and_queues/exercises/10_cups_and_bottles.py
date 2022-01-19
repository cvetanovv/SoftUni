from collections import deque

cups_capacity = deque([int(num) for num in input().split()])
bottles_capacity = [int(num) for num in input().split()]
wasted_liters = 0

while cups_capacity and bottles_capacity:
    cup = cups_capacity.popleft()
    bottle = bottles_capacity.pop()

    if bottle >= cup:
        wasted_water = bottle - cup
        wasted_liters += wasted_water
    else:
        cups_capacity.appendleft(cup - bottle)

if bottles_capacity:
    print(f"Bottles: {' '.join(str(num) for num in bottles_capacity)}")
elif cups_capacity:
    print(f"Cups: {' '.join(str(num) for num in cups_capacity)}")
print(f"Wasted litters of water: {wasted_liters}")