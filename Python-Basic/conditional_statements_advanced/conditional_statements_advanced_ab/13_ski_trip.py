days_in_hotel = int(input())
room = input()
rating = input()

vacancy_cost = 0

if room == 'room for one person':
    vacancy_cost = (days_in_hotel - 1) * 18

elif room == 'apartment':
    vacancy_cost = (days_in_hotel - 1) * 25
    if days_in_hotel < 10:
        vacancy_cost -= vacancy_cost * 0.30
    elif 10 <= days_in_hotel <= 15:
        vacancy_cost -= vacancy_cost * 0.35
    elif days_in_hotel > 15:
        vacancy_cost -= vacancy_cost * 0.50

elif room == 'president apartment':
    vacancy_cost = (days_in_hotel - 1) * 35
    if days_in_hotel < 10:
        vacancy_cost -= vacancy_cost * 0.10
    elif 10 <= days_in_hotel <= 15:
        vacancy_cost -= vacancy_cost * 0.15
    elif days_in_hotel > 15:
        vacancy_cost -= vacancy_cost * 0.20

if rating == 'positive':
    vacancy_cost += vacancy_cost * 0.25
elif rating == 'negative':
    vacancy_cost -= vacancy_cost * 0.10

print(f"{vacancy_cost:.2f}")