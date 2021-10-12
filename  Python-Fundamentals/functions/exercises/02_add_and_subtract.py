def sum_number(first_num, second_num):
    return first_num + second_num


def subtract(sum_of_num, third_num):
    return sum_of_num - third_num


def add_and_subtract(first_num, second_num, third_num):
    sum_of_first_two_numbers = sum_number(first_num, second_num)
    result = subtract(sum_of_first_two_numbers, third_num)
    return result


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))