houses = [int(num) for num in input().split("@")]

cupid_position = 0
count_failed_houses = 0

while True:
    command = input()
    if command == "Love!":
        print(f"Cupid's last position was {cupid_position}.")
        if sum(houses) == 0:
            print(f"Mission was successful.")
        else:
            for failed_house in houses:
                if failed_house != 0:
                    count_failed_houses += 1
            print(f"Cupid has failed {count_failed_houses} places.")
        break
    command = command.split()
    jump = int(command[1])
    cupid_position += jump
    if cupid_position >= len(houses):
        cupid_position = 0
    if houses[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")
        continue
    houses[cupid_position] -= 2
    if houses[cupid_position] <= 0:
        print(f"Place {cupid_position} has Valentine's day.")
        houses[cupid_position] = 0