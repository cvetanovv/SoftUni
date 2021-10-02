list_of_numbers = input().split()
list_of_opposite_numbers = []

for string_number in list_of_numbers:
    list_of_opposite_numbers.append(-int(string_number))

print(list_of_opposite_numbers)