rolls_paper = int(input())
rolls_cloth = int(input())
liters_glue = float(input())
percent_discount = float(input())

price_materials = (rolls_paper * 5.80) + (rolls_cloth * 7.20) + (liters_glue * 1.20)
percent_discount /= 100
price_materials -= price_materials * percent_discount
print(f"{price_materials:.3f}")
