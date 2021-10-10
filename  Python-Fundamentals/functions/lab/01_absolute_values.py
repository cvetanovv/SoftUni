def abs_list(values):
    list_of_abs_values = []
    for number in values:
        number = float(number)
        if number < 0:
            number = number * -1
        list_of_abs_values.append(number)
    return list_of_abs_values


list_of_numbers = input().split(' ')

print(abs_list(list_of_numbers))