import math
number_days = int(input())
leftover_food_kg = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_gram = float(input())

dog_needed_food = number_days * dog_food_per_day_kg
cat_needed_food = number_days * cat_food_per_day_kg
turtle_needed_food = (number_days * turtle_food_per_day_gram) / 1000

total_food = dog_needed_food + cat_needed_food + turtle_needed_food
food = 0

if leftover_food_kg >= total_food:
    food = leftover_food_kg - total_food
    print(f"{math.floor(food)} kilos of food left.")
elif total_food > leftover_food_kg:
    food = total_food - leftover_food_kg
    print(f"{math.ceil(food)} more kilos of food are needed.")