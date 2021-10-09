def price_of_order(product, quantity):
    final_price = 0
    if product == "coffee":
        final_price = quantity * 1.5
    elif product == "water":
        final_price = quantity * 1.00
    elif product == "coke":
        final_price = quantity * 1.40
    elif product == "snacks":
        final_price = quantity * 2.00
    return f"{final_price:.2f}"


type_of_product = input()
quantity = int(input())

print(price_of_order(type_of_product, quantity))