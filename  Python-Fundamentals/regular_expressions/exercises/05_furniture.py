import re

some_text = input()
pattern = r">>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)"
list_of_furniture = []
total_price = 0

while some_text != "Purchase":
    match = re.search(pattern, some_text)
    if match:
        furniture, price, quantity = match.groups()
        list_of_furniture.append(furniture)
        total_price += float(price) * int(quantity)
    some_text = input()

print("Bought furniture:")
for item in list_of_furniture:
    print(item)
print(f"Total money spend: {total_price:.2f}")