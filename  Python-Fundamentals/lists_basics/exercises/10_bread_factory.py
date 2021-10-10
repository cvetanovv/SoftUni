working_days = input().split("|")

energy = 100
coins = 100

for working_day in working_days:
    day = working_day.split('-')
    event = day[0]
    number = int(day[1])

    if event == 'rest':
        if (energy + number) >= 100:
            print(f"You gained {100 - energy} energy.")
            print("Current energy: 100.")
            energy = 100
        else:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
    elif event == 'order':
        if energy - 30 < 0:
            print("You had to rest!")
            energy += 50
        else:
            energy -= 30
            print(f"You earned {number} coins.")
            coins += number
    else:
        if coins - number > 0:
            print(f"You bought {event}.")
            coins -= number
        else:
            print(f"Closed! Cannot afford {event}.")
            exit()

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")