inventory = [x for x in input().split(", ")]


while True:
    command = input()
    if command == "Craft!":
        print(", ".join(inventory))
        break
    command = command.split(" - ")
    action = command[0]
    item = command[1]

    if action == "Collect":
        if item in inventory:
            continue
        else:
            inventory.append(item)
    if action == "Drop":
        if item in inventory:
            inventory.remove(item)
    if action == "Combine Items":
        combine_items = item.split(":")
        old_item = combine_items[0]
        new_item = combine_items[1]
        if old_item in inventory:
            old_item_index = inventory.index(old_item)
            inventory.insert(old_item_index + 1, new_item)
    if action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)