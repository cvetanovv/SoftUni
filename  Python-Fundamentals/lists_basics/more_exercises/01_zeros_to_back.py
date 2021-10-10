numbers = input().split(", ")

for number in numbers:
    if number == "0":
        numbers.remove(number)
        numbers.append("0")

final_list = []
for number in numbers:
    final_list.append(int(number))

print(final_list)