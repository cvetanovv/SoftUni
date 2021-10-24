number_of_days = int(input())
number_of_players = int(input())
group_energy = float(input())
water_per_day_one_person = float(input())
food_per_day_one_person = float(input())

total_water = water_per_day_one_person * number_of_days * number_of_players
total_food = food_per_day_one_person * number_of_days * number_of_players


for day in range(1, number_of_days + 1):
    energy_loss = float(input())
    group_energy -= energy_loss
    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
        exit()
    if day % 2 == 0:
        group_energy *= 1.05
        total_water *= 0.70
    if day % 3 == 0:
        total_food -= total_food / number_of_players
        group_energy *= 1.10

print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")