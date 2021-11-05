country = input().split(", ")
capitals = input().split(", ")

country_with_capitals = dict(zip(country, capitals))

for country, capital in country_with_capitals.items():
    print(f"{country} -> {capital}")