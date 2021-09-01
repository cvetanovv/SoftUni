budget = float(input())
season = input()

type_of_car = ''
car_class = ''
price = 0

if budget <= 100:
    car_class = 'Economy class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        type_of_car = 'Jeep'
        price = budget * 0.65

elif 100 < budget <= 500:
    car_class = 'Compact class'
    if season == 'Summer':
        type_of_car = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        type_of_car = 'Jeep'
        price = budget * 0.80

elif budget > 500:
    car_class = 'Luxury class'
    type_of_car = 'Jeep'
    price = budget * 0.90

print(f"{car_class}")
print(f"{type_of_car} - {price:.2f}")