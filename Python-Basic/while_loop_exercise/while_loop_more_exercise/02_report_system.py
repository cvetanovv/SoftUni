needed_sum = int(input())

cash_payment = 0
cash_counter = 0
card_payment = 0
card_counter = 0
counter = 1
all_sum = 0

while True:
    object_prices = input()
    if object_prices == 'End':
        print('Failed to collect required money for charity.')
        break

    object_prices = int(object_prices)
    if counter % 2 == 1:
        if object_prices > 100:
            print('Error in transaction!')
        else:
            cash_payment += object_prices
            cash_counter += 1
            all_sum += object_prices
            print('Product sold!')
    if counter % 2 == 0:
        if object_prices < 10:
            print('Error in transaction!')
        else:
            card_payment += object_prices
            card_counter += 1
            all_sum += object_prices
            print('Product sold!')
    if all_sum >= needed_sum:
        print(f"Average CS: {cash_payment / cash_counter:.2f}")
        print(f"Average CC: {card_payment / card_counter:.2f}")
        break
    counter += 1