fuel = input()
liters = float(input())
club_card = input()

fuel_price = 0

if fuel == 'Gas':
    if club_card == 'Yes':
        fuel_price = liters * 0.85
    elif club_card == 'No':
        fuel_price = liters * 0.93

elif fuel == 'Gasoline':
    if club_card == 'Yes':
        fuel_price = liters * 2.04
    elif club_card == 'No':
        fuel_price = liters * 2.22

elif fuel == 'Diesel':
    if club_card == 'Yes':
        fuel_price = liters * 2.21
    elif club_card == 'No':
        fuel_price = liters * 2.33

if 20 <= liters <= 25:
    fuel_price -= fuel_price * 0.08
elif liters > 25:
    fuel_price -= fuel_price * 0.10

print(f"{fuel_price:.2f} lv.")