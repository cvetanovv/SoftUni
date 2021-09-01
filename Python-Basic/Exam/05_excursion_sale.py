holidays_sea = int(input())
holidays_mountain = int(input())

profit = 0

while True:
    if holidays_sea == 0 and holidays_mountain == 0:
        print("Good job! Everything is sold.")
        print(f"Profit: {profit} leva.")
        break
    type_holiday = input()
    if type_holiday == "Stop":
        print(f"Profit: {profit} leva.")
        break

    if type_holiday == "sea":
        if holidays_sea > 0:
            profit += 680
            holidays_sea -= 1
        else:
            continue
    elif type_holiday == 'mountain':
        if holidays_mountain > 0:
            profit += 499
            holidays_mountain -= 1
        else:
            continue
