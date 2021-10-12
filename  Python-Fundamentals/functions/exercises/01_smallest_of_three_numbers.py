def smallest_number(first_num, second_num, third_num):
    numbers = [first_num, second_num, third_num]
    smallest_num = min(numbers)
    return smallest_num


first_number = int(input())
second_number = int(input())
third_number = int(input())

min_number = smallest_number(first_number, second_number, third_number)
print(min_number)
