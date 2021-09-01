import math
num_magnoli = int(input())
num_ziumbiuli = int(input())
num_rose = int(input())
num_cactus = int(input())
gift_price = float(input())

sum = (num_magnoli * 3.25) + (num_ziumbiuli * 4) + (num_rose * 3.50) + (num_cactus * 8)
sum -= sum * 0.05
money = 0

if sum >= gift_price:
    money = sum - gift_price
    print(f"She is left with {math.floor(money)} leva.")
else:
    money = gift_price - sum
    print(f"She will have to borrow {math.ceil(money)} leva.")