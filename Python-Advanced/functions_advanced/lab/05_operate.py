from functools import reduce


def operate(operator, *numbers):
    if operator == "+":
        return sum(numbers)
    elif operator == "-":
        result = reduce((lambda x, y: x - y), numbers)
        return result
    elif operator == "*":
        result = 1
        for num in numbers:
            result = result * num
        return result
    elif operator == "/":
        try:
            result = reduce((lambda x, y: x / y), numbers)
            return result
        except ZeroDivisionError:
            pass


print(operate("+", 1, 2, 3))
print(operate("/", 3, 4))