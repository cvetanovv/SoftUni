products_dic = {}

while True:
    command = input()
    if command == "statistics":
        break
    command = command.split(": ")

    product = command[0]
    quantity = int(command[1])

    if product not in products_dic:
        products_dic[product] = quantity
    else:
        products_dic[product] += quantity

print("Products in stock:")
for key, value in products_dic.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products_dic)}")
print(f"Total Quantity: {sum(products_dic.values())}")