price_per_kg_vegetable = float(input())
price_per_kg_fruit = float(input())
all_amount_vegetable = float(input())
all_amount_fruit = float(input())

price_vegetable = price_per_kg_vegetable * all_amount_vegetable
price_fruit = price_per_kg_fruit * all_amount_fruit
money_in_lev = price_fruit + price_vegetable
money_in_euro = money_in_lev / 1.94
print(format(money_in_euro, '.2f'))