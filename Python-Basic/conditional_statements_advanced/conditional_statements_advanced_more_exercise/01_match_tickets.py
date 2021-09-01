budget = float(input())
category = input()
number_of_people = int(input())

budget_after_transport = 0

if 1 <= number_of_people <= 4:
    budget_after_transport = budget * 0.25
elif 5 <= number_of_people <= 9:
    budget_after_transport = budget * 0.40
elif 10 <= number_of_people <= 24:
    budget_after_transport = budget * 0.50
elif 25 <= number_of_people <= 49:
    budget_after_transport = budget * 0.60
elif number_of_people >= 50:
    budget_after_transport = budget * 0.75

money_for_tickets = 0

if category == 'VIP':
    money_for_tickets = 499.99 * number_of_people
elif category == 'Normal':
    money_for_tickets = 249.99 * number_of_people

all_money = abs(money_for_tickets - budget_after_transport)

if budget_after_transport >= money_for_tickets:
    print(f"Yes! You have {all_money:.2f} leva left.")
else:
    print(f"Not enough money! You need {all_money:.2f} leva.")