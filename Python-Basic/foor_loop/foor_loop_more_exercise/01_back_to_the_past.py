inherited_money = float(input())
year_need_to_live = int(input())

age = 18

for year in range(1800, year_need_to_live + 1):
    if year % 2 == 0:
        inherited_money -= 12000
    elif year % 2 == 1:
        inherited_money -= (12000 + (age * 50))
    age += 1

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")