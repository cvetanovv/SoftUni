friends = [friend for friend in input().split(", ")]

while True:
    command = input()
    if command == "Report":
        break
    command = command.split()
    action = command[0]
    index = command[1]
    if action == "Blacklist":
        if index not in friends:
            print(f"{index} was not found.")
        else:
            print(f"{index} was blacklisted.")
            friend_index = friends.index(index)
            friends[friend_index] = "Blacklisted"
    if action == "Error":
        index = int(index)
        if 0 <= index < len(friends):
            if friends[index] != "Blacklisted" and friends[index] != "Lost":
                print(f"{friends[index]} was lost due to an error.")
                friends[index] = "Lost"
    if action == "Change":
        index = int(index)
        new_name = command[2]
        if 0 <= index < len(friends):
            print(f"{friends[index]} changed his username to {new_name}.")
            friends[index] = new_name

blacklist_counter = 0
lost_counter = 0

for name in friends:
    if name == "Blacklisted":
        blacklist_counter += 1
    if name == "Lost":
        lost_counter += 1

print(f"Blacklisted names: {blacklist_counter}")
print(f"Lost names: {lost_counter}")
print(" ".join(friends))