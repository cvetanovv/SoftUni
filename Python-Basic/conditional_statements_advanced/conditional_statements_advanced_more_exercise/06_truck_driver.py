season = input()
km_per_month = float(input())

money = 0

if km_per_month <= 5000:
    if season == 'Spring' or season == 'Autumn':
        money = (km_per_month * 0.75) * 4
    elif season == 'Summer':
        money = (km_per_month * 0.90) * 4
    elif season == 'Winter':
        money = (km_per_month * 1.05) * 4
elif 5000 < km_per_month <= 10000:
    if season == 'Spring' or season == 'Autumn':
        money = (km_per_month * 0.95) * 4
    elif season == 'Summer':
        money = (km_per_month * 1.10) * 4
    elif season == 'Winter':
        money = (km_per_month * 1.25) * 4
elif km_per_month > 10000:
    money = (km_per_month * 1.45) * 4


money_after_tax = money * 0.90
print(f"{money_after_tax:.2f}")