flowers = input()
numbers_of_flowers = int(input())
budget = int(input())

price = 0

if flowers == 'Roses':
    price = numbers_of_flowers * 5
    if numbers_of_flowers > 80:
        price -= price * 0.10
elif flowers == 'Dahlias':
    price = numbers_of_flowers * 3.80
    if numbers_of_flowers > 90:
        price -= price * 0.15
elif flowers == 'Tulips':
    price = numbers_of_flowers * 2.80
    if numbers_of_flowers > 80:
        price -= price * 0.15
elif flowers == 'Narcissus':
    price = numbers_of_flowers * 3
    if numbers_of_flowers < 120:
        price += price * 0.15
elif flowers == 'Gladiolus':
    price = numbers_of_flowers * 2.5
    if numbers_of_flowers < 80:
        price += price * 0.20


if budget >= price:
    sum = budget - price
    print(f"Hey, you have a great garden with {numbers_of_flowers} {flowers} and {sum:.2f} leva left.")
else:
    sum = price - budget
    print(f"Not enough money, you need {sum:.2f} leva more.")