number = input()

list_numbers = []
for num in number:
    list_numbers.append(num)

list_numbers.sort(reverse=True)
largest_numbers = ''.join(list_numbers)
print(largest_numbers)