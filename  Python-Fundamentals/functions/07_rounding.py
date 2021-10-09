def round_numbers(list_of_numbers):
    rounded_list = []
    for number in list_of_numbers:
        number = round(float(number))
        rounded_list.append(number)
    return rounded_list


numbers = input().split()

print(round_numbers(numbers))