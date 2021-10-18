def multiplication_output(first_num, second_num, third_num):
    if first_num == 0 or second_num == 0 or third_num == 0:
        return 'zero'
    elif first_num < 0 or second_num < 0 or third_num < 0:
        return 'negative'
    else:
        return 'positive'


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication_output(first_number, second_number, third_number))