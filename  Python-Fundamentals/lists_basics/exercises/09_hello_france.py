items_with_prices = input().split("|")
budget = float(input())

train_ticket = 150
saved_money = 0
profit = 0
price_of_selling_items = []

for item_with_price in items_with_prices:
    item_and_price = item_with_price.split("->")
    item = item_and_price[0]
    price = float(item_and_price[1])

    if item == 'Clothes':
        if price <= 50:
            if budget - price >= 0:
                budget -= price
                new_price = price * 1.40
                profit += new_price - price
                saved_money += new_price
                price_of_selling_items.append(new_price)
    elif item == 'Shoes':
        if price <= 35:
            if budget - price >= 0:
                budget -= price
                new_price = price * 1.40
                profit += new_price - price
                saved_money += new_price
                price_of_selling_items.append(new_price)
    elif item == 'Accessories':
        if price <= 20.50:
            if budget - price >= 0:
                budget -= price
                new_price = price * 1.40
                profit += new_price - price
                saved_money += new_price
                price_of_selling_items.append(new_price)

for price in price_of_selling_items:
    print(f"{price:.2f}", end=' ')

print()
print(f"Profit: {profit:.2f}")

saved_money += budget
if saved_money >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")
