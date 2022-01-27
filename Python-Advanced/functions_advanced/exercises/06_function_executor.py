def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    final_numbers = []
    for func, nums in args:
        result = func(*nums)
        final_numbers.append(result)
    return final_numbers


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
