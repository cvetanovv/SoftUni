numbers = [float(num) for num in input().split()]

dict_occurrences = {}

for number in numbers:
    if number not in dict_occurrences:
        dict_occurrences[number] = 0
    dict_occurrences[number] += 1

for num, frequency in dict_occurrences.items():
    print(f"{num} - {frequency} times")