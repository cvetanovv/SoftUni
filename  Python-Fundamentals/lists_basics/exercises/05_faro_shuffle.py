deck_of_cards = input().split()
number_of_shuffles = int(input())

new_deck = deck_of_cards
middle_of_deck = len(new_deck) // 2

for shuffle in range(number_of_shuffles):
    first_half = new_deck[:middle_of_deck]
    second_half = new_deck[middle_of_deck::]
    new_deck = []
    for card_index in range(len(first_half)):
        new_deck.append(first_half[card_index])
        new_deck.append(second_half[card_index])

print(new_deck)