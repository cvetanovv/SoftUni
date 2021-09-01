needed_money_for_vacation = float(input())
money_on_hand = float(input())

days_counter = 0
spend_days_counter = 0

while True:
    spend_or_save = input()
    money_spend_or_save = float(input())
    days_counter += 1

    if spend_or_save == 'spend':
        money_on_hand -= money_spend_or_save
        if money_on_hand < 0:
            money_on_hand = 0
        spend_days_counter += 1
    elif spend_or_save == 'save':
        money_on_hand += money_spend_or_save
        spend_days_counter = 0

    if spend_days_counter == 5:
        print("You can't save the money.")
        print(days_counter)
        break
    if money_on_hand >= needed_money_for_vacation:
        print(f"You saved the money for {days_counter} days.")
        break
