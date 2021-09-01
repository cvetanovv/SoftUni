price_skumria_kg = float(input())
price_caca_kg = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = float(input())

price_palamud_kg =  price_skumria_kg * 1.6
sum_palamud = price_palamud_kg * kg_palamud

price_safrid_kg = price_caca_kg * 1.8
sum_safrid = price_safrid_kg * kg_safrid

sum_midi = kg_midi * 7.5

all_sum = sum_palamud + sum_safrid + sum_midi
all_sum = format(all_sum, '.2f')
print(all_sum)