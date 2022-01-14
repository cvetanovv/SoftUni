from collections import deque

quantity_of_food = int(input())
food_per_order = deque(int(num) for num in input().split(" "))
print(max(food_per_order))

while food_per_order:
    if quantity_of_food - food_per_order[0] >= 0:
        removed_food = food_per_order.popleft()
        quantity_of_food -= removed_food
    else:
        break

if food_per_order:
    food_as_string = [str(food) for food in food_per_order]
    print(f"Orders left: {' '.join(food_as_string)}")
else:
    print("Orders complete")
