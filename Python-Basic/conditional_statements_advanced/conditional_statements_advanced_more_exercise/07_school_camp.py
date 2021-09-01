season = input()
group_gender = input()
students_number = int(input())
nights = int(input())

sport = ''
price = 0

if season == 'Winter':
    if group_gender == 'girls':
        price = nights * 9.60 * students_number
        sport = 'Gymnastics'
    elif group_gender == 'boys':
        price = nights * 9.60 * students_number
        sport = 'Judo'
    elif group_gender == 'mixed':
        price = nights * 10 * students_number
        sport = 'Ski'

elif season == 'Spring':
    if group_gender == 'girls':
        price = nights * 7.20 * students_number
        sport = 'Athletics'
    elif group_gender == 'boys':
        price = nights * 7.20 * students_number
        sport = 'Tennis'
    elif group_gender == 'mixed':
        price = nights * 9.50 * students_number
        sport = 'Cycling'

elif season == 'Summer':
    if group_gender == 'girls':
        price = nights * 15 * students_number
        sport = 'Volleyball'
    elif group_gender == 'boys':
        price = nights * 15 * students_number
        sport = 'Football'
    elif group_gender == 'mixed':
        price = nights * 20 * students_number
        sport = 'Swimming'

if 10 <= students_number < 20:
    price -= price * 0.05
elif 20 <= students_number < 50:
    price -= price * 0.15
elif students_number >= 50:
    price -= price * 0.50

print(f"{sport} {price:.2f} lv.")
