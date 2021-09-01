budget = float(input())
statisti = int(input())
price_clothing_per_statist = float(input())

decor = budget * 0.10
sum_for_clothing = statisti * price_clothing_per_statist

if statisti > 150:
    sum_for_clothing *= 0.90

all_sum_need_for_movie = decor + sum_for_clothing
sum_left = budget - all_sum_need_for_movie

if all_sum_need_for_movie > budget:
    print('Not enough money!')
    print(f"Wingard needs {abs(sum_left):.2f} leva more.")
else:
    print('Action!')
    print(f"Wingard starts filming with {sum_left:.2f} leva left.")