budget = float(input())
season = input()
number_of_fishermen = int(input())

cost = 0

if season == 'Spring':
    if number_of_fishermen <= 6:
        cost = 3000 * 0.90
    elif 7 <= number_of_fishermen <= 11:
        cost = 3000 * 0.85
    elif number_of_fishermen >= 12:
        cost = 3000 * 0.75

    if number_of_fishermen % 2 == 0:
        cost -= cost * 0.05
elif season == 'Summer':
    if number_of_fishermen <= 6:
        cost = 4200 * 0.90
    elif 7 <= number_of_fishermen <= 11:
        cost = 4200 * 0.85
    elif number_of_fishermen >= 12:
        cost = 4200 * 0.75

    if number_of_fishermen % 2 == 0:
        cost -= cost * 0.05
elif season == 'Autumn':
    if number_of_fishermen <= 6:
        cost = 4200 * 0.90
    elif 7 <= number_of_fishermen <= 11:
        cost = 4200 * 0.85
    elif number_of_fishermen >= 12:
        cost = 4200 * 0.75
elif season == 'Winter':
    if number_of_fishermen <= 6:
        cost = 2600 * 0.90
    elif 7 <= number_of_fishermen <= 11:
        cost = 2600 * 0.85
    elif number_of_fishermen >= 12:
        cost = 2600 * 0.75

    if number_of_fishermen % 2 == 0:
        cost -= cost * 0.05

money = abs(budget - cost)
if budget >= cost:
    print(f"Yes! You have {money:.2f} leva left.")
elif cost > budget:
    print(f"Not enough money! You need {money:.2f} leva.")