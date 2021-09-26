budget = float(input())
price_per_kg_flour = float(input())
price_one_pack_egg = price_per_kg_flour * 0.75
price_of_milk = (price_per_kg_flour * 1.25) / 4
price_of_one_bread = price_one_pack_egg + price_of_milk + price_per_kg_flour

bread = 0
colored_eggs = 0

while True:
    if price_of_one_bread > budget:
        print(f"You made {bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        break
    budget -= price_of_one_bread
    bread += 1
    colored_eggs += 3
    if bread % 3 == 0:
        colored_eggs -= bread - 2