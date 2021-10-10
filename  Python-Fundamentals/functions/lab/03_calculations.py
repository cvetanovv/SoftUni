def calculations(operator, first_number, second_number):
    result = 0
    if operator == "multiply":
        result = first_number * second_number
    elif operator == 'divide':
        result = first_number / second_number
    elif operator == 'add':
        result = first_number + second_number
    elif operator == 'subtract':
        result = first_number - second_number
    return int(result)


operator = input()
first_num = int(input())
second_num = int(input())

print(calculations(operator, first_num, second_num))