trip_price = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bear_count = int(input())
minions_count = int(input())
truck_count = int(input())

puzzle_sum = puzzle_count * 2.60
dolls_sum = dolls_count * 3
bear_sum = bear_count * 4.10
minions_sum = minions_count * 8.20
truck_sum = truck_count * 2

all_sum = puzzle_sum + dolls_sum + bear_sum + minions_sum + truck_sum
toys_number = puzzle_count + dolls_count + bear_count + minions_count + truck_count

if toys_number >= 50:
    all_sum = all_sum * 0.75

all_sum = all_sum * 0.90

if all_sum >= trip_price:
    left_money = all_sum - trip_price
    print(f"Yes! {left_money:.2f} lv left.")
else:
    needed_money = trip_price - all_sum
    print(f"Not enough money! {needed_money:.2f} lv needed.")