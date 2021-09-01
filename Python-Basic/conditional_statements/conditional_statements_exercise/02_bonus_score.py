number = float(input())

bonus_num = 0
if number <= 100:
    bonus_num = 5
elif 100 < number <= 1000:
    bonus_num = number * 0.20
else:
    bonus_num = number * 0.10

if number % 2 == 0:
    bonus_num += 1
if number % 10 == 5:
    bonus_num += 2

print(bonus_num)
print(bonus_num + number)