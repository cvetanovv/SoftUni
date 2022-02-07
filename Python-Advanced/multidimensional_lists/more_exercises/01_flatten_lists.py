numbers = input().split("|")

list_of_numbers = []

while numbers:
    sublist = numbers.pop().split()
    for el in sublist:
        list_of_numbers.append(el)

print(*list_of_numbers, sep= " ")
