products = {}

while True:
    command = input()
    if command == "buy":
        break
    command = command.split()
    product_name = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product_name not in products:
        products[product_name] = [price, quantity]
    else:
        products[product_name][0] = price
        products[product_name][1] += quantity

for product, final_price in products.items():
    total_price = final_price[0] * final_price[1]
    print(f"{product} -> {total_price:.2f}")
