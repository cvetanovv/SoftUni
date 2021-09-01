kilometers = int(input())
part_of_day = input()

if kilometers < 20:
    if part_of_day == 'day':
        price = 0.70 + kilometers * 0.79
        print(f"{price:.2f}")
    elif part_of_day == 'night':
        price = 0.70 + kilometers * 0.90
        print(f"{price:.2f}")
elif kilometers < 100:
    price = kilometers * 0.09
    print(f"{price:.2f}")
else:
    price = kilometers * 0.06
    print(f"{price:.2f}")