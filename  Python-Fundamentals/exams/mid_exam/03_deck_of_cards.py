list_of_cards = [card for card in input().split(", ")]
number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split(", ")
    action = command[0]
    if action == "Add":
        card_name = command[1]
        if card_name in list_of_cards:
            print("Card is already in the deck")
        else:
            print("Card successfully added")
            list_of_cards.append(card_name)
    if action == "Remove":
        card_name = command[1]
        if card_name not in list_of_cards:
            print("Card not found")
        else:
            print("Card successfully removed")
            list_of_cards.remove(card_name)
    if action == "Remove At":
        index = int(command[1])
        if 0 <= index < len(list_of_cards):
            list_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print(f"Index out of range")
    if action == "Insert":
        index = int(command[1])
        card_name = command[2]
        if 0 <= index < len(list_of_cards):
            if card_name in list_of_cards:
                print("Card is already added")
            else:
                list_of_cards.insert(index, card_name)
                print("Card successfully added")
        else:
            print("Index out of range")

print(", ".join(list_of_cards))