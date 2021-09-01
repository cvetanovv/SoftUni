number_of_detergents = int(input())
detergents_in_ml = number_of_detergents * 750

counter = 0
dishes = 0
pots = 0

while True:
    number_washing_dishes = input()
    if number_washing_dishes == 'End' or detergents_in_ml == 0:
        print("Detergent was enough!")
        print(f"{dishes} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {detergents_in_ml} ml.")
        break

    number_washing_dishes = int(number_washing_dishes)
    counter += 1
    if counter % 3 == 0:
        detergents_in_ml -= number_washing_dishes * 15
        pots += number_washing_dishes
    else:
        detergents_in_ml -= number_washing_dishes * 5
        dishes += number_washing_dishes
    if detergents_in_ml < 0:
        print(f"Not enough detergent, {abs(detergents_in_ml)} ml. more necessary!")
        break
