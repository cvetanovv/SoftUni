string_of_numbers = input().split(", ")
count_of_beggars = int(input())

list_of_numbers = []
for num in string_of_numbers:
    list_of_numbers.append(int(num))

final_list = []
money = 0

for beggar in range(count_of_beggars):
    for i in range(beggar, len(string_of_numbers) + 1, count_of_beggars):
        if i >= len(list_of_numbers):
            break
        money += list_of_numbers[i]
    final_list.append(money)
    money = 0

print(final_list)