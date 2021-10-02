factor_number = int(input())
count_number = int(input())

list_of_numbers = []

for number in range(1, count_number + 1):
    number *= factor_number
    list_of_numbers.append(number)

print(list_of_numbers)