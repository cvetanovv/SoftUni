string_of_numbers = input().split()
numbers_to_remove = int(input())
list_of_numbers = []
for num in string_of_numbers:
    list_of_numbers.append(int(num))

for number in range(numbers_to_remove):
    list_of_numbers.remove(min(list_of_numbers))

print(*list_of_numbers, sep=', ')
