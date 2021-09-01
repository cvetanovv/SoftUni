import sys

number = input()

bigest_number = -sys.maxsize

while number != 'Stop':
    number = int(number)
    if number >= bigest_number:
        bigest_number = number
    number = input()

print(bigest_number)