age = int(input())
laundry_price = float(input())
toy_price = float(input())

toys = 0
saved_money = 0

for x in range(1, age + 1):
    if x % 2 == 0:
        saved_money += (x * 10 / 2) - 1
    else:
        toys += 1

all_money = (toys * toy_price) + saved_money
diff = abs(all_money - laundry_price)

if all_money >= laundry_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")