days = int(input())

all_liters_rakia = 0
all_degrees = 0

for day in range(days):
    liters_rakia = float(input())
    degrees = float(input())

    all_liters_rakia += liters_rakia
    all_degrees += liters_rakia * degrees

average_degrees = all_degrees / all_liters_rakia

print(f"Liter: {all_liters_rakia:.2f}")
print(f"Degrees: {average_degrees:.2f}")
if average_degrees < 38:
    print("Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print("Super!")
elif average_degrees > 42:
    print("Dilution with distilled water!")