contacts = {}
last_command = 0

while True:
    command = input()
    if command[0].isdigit():
        last_command = int(command)
        break
    command = command.split("-")
    name = command[0]
    number = command[1]
    contacts[name] = number

for i in range(last_command):
    searching_name = input()
    if searching_name not in contacts.keys():
        print(f"Contact {searching_name} does not exist.")
    else:
        print(f"{searching_name} -> {contacts[searching_name]}")