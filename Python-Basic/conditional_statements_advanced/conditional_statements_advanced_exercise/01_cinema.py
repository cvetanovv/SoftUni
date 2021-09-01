screening_type = input()
rows = int(input())
colums = int(input())

room_seats = rows * colums
income = 0

if screening_type == 'Premiere':
    income = room_seats * 12
elif screening_type == 'Normal':
    income = room_seats * 7.50
elif screening_type == 'Discount':
    income = room_seats * 5

print(f"{income:.2f}")