weight = float(input())
type_of_service = input()
distance_in_km = int(input())

price = 0
overprice = 0

if type_of_service == "standard":
    if weight < 1:
        price = distance_in_km * 0.03
    elif 1 <= weight < 10:
        price = distance_in_km * 0.05
    elif 10 <= weight < 40:
        price = distance_in_km * 0.10
    elif 40 <= weight < 90:
        price = distance_in_km * 0.15
    elif 90 <= weight < 150:
        price = distance_in_km * 0.20

if type_of_service == "express":
    if weight < 1:
        overprice = ((0.03 * 0.80) * weight) * distance_in_km
        price = (distance_in_km * 0.03) + overprice
    elif 1 <= weight < 10:
        overprice = ((0.05 * 0.40) * weight) * distance_in_km
        price = (distance_in_km * 0.05) + overprice
    elif 10 <= weight < 40:
        overprice = ((0.10 * 0.05) * weight) * distance_in_km
        price = (distance_in_km * 0.10) + overprice
    elif 40 <= weight < 90:
        overprice = ((0.15 * 0.02) * weight) * distance_in_km
        price = (distance_in_km * 0.15) + overprice
    elif 90 <= weight < 150:
        overprice = ((0.20 * 0.01) * weight) * distance_in_km
        price = (distance_in_km * 0.20) + overprice

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {price:.2f} lv.")