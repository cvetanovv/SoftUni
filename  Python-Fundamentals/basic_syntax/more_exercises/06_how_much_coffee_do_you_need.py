coffee = 0

while True:
    if coffee == 6:
        print("You need extra sleep")
        break
    command = input()
    if command == "END":
        print(coffee)
        break
    if command == "dog":
        coffee += 1
    if command == "DOG":
        coffee += 2
    if command == "cat":
        coffee += 1
    if command == "CAT":
        coffee += 2
    if command == "coding":
        coffee += 1
    if command == "CODING":
        coffee += 2
    if command == "movie":
        coffee += 1
    if command == "MOVIE":
        coffee += 2
