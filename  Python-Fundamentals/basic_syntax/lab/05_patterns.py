number = int(input())

rows = ''
for _ in range(number):
    rows += '*'
    print(rows)
for star_numbers in range(number, 0, -1):
    print(rows[:star_numbers - 1])