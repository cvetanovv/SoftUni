budget = float(input())
season = input()

destination = ''
place_to_rest = ''
amount_spend = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place_to_rest = 'Camp'
        amount_spend = budget * 0.30
    elif season == 'winter':
        place_to_rest = 'Hotel'
        amount_spend = budget * 0.70

elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place_to_rest = 'Camp'
        amount_spend = budget * 0.40
    elif season == 'winter':
        place_to_rest = 'Hotel'
        amount_spend = budget * 0.80

elif budget > 1000:
    destination = 'Europe'
    amount_spend = budget * 0.90
    place_to_rest = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{place_to_rest} - {amount_spend:.2f}")