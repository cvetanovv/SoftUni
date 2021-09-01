price_strawberries_kg = float(input())
kg_bananas = float(input())
kg_oranges = float(input())
kg_rasberries = float(input())
kg_strawberries = float(input())

price_rasberries = price_strawberries_kg / 2
price_oranges = price_rasberries * 0.60
price_bananas = price_rasberries * 0.20

sum_rasberries = kg_rasberries * price_rasberries
sum_oranges = kg_oranges * price_oranges
sum_bananas = kg_bananas * price_bananas
sum_strawberries = kg_strawberries * price_strawberries_kg

all_summ = sum_rasberries + sum_oranges + sum_bananas + sum_strawberries
print(all_summ)
