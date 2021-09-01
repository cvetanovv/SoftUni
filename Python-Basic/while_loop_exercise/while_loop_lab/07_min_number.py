import  sys

number = input()

min_num = sys.maxsize

while number != 'Stop':
    number = int(number)
    if number <= min_num:
        min_num = number
    number = input()

print(min_num)