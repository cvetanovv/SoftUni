hrizantemi = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price = 0
all_flowers = hrizantemi + roses + tulips


if season == 'Spring':
    price = (2 * hrizantemi) + (roses * 4.1) + (tulips * 2.50)
    if holiday == 'Y':
        price += price * 0.15
    if tulips > 7:
        price -= price * 0.05
elif season == 'Summer':
    price = (2 * hrizantemi) + (roses * 4.1) + (tulips * 2.50)
    if holiday == 'Y':
        price += price * 0.15
elif season == 'Autumn':
    price = (3.75 * hrizantemi) + (roses * 4.5) + (tulips * 4.15)
    if holiday == 'Y':
        price += price * 0.15
elif season == 'Winter':
    price = (3.75 * hrizantemi) + (roses * 4.5) + (tulips * 4.15)
    if holiday == 'Y':
        price += price * 0.15
    if roses >= 10:
        price -= price * 0.10




if all_flowers > 20:
    price -= price * 0.20

price += 2

print(f"{price:.2f}")