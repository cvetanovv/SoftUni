number_of_cars = int(input())

parking = {}

for _ in range(number_of_cars):
    command = input().split()
    action = command[0]
    if action == "register":
        name, plate_number = command[1], command[2]
        if name not in parking:
            parking[name] = plate_number
            print(f"{name} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    if action == "unregister":
        username = command[1]
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for user, plate in parking.items():
    print(f"{user} => {plate}")
