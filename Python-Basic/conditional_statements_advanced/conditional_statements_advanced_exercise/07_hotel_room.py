months = input()
nights = int(input())

studio = 0
apartment = 0

if months == 'May' or months == 'October':
    studio = 50 * nights
    apartment = 65 * nights
    if 7 < nights <= 14:
        studio -= studio * 0.05
    elif nights > 14:
        studio -= studio * 0.30
        apartment -= apartment * 0.10

elif months == 'June' or months == 'September':
    studio = 75.20 * nights
    apartment = 68.70 * nights
    if nights > 14:
        studio -= studio * 0.20
        apartment -= apartment * 0.10

elif months == 'July' or months == 'August':
    studio = 76 * nights
    apartment = 77 * nights
    if nights > 14:
        apartment -= apartment * 0.10

print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")