from functools import reduce

expression = input().split()

operators = "*", "+", "-", "/"
numbers = []

for char in expression:
    if char in operators:
        if char == "+":
            numbers = [sum(numbers)]
        elif char == "*":
            result = 1
            for num in numbers:
                result *= num
            numbers.clear()
            numbers.append(result)
        elif char == "-":
            result = reduce((lambda x, y: x - y), numbers)
            numbers.clear()
            numbers.append(result)
        elif char == "/":
            result = reduce((lambda x, y: x // y), numbers)
            numbers.clear()
            numbers.append(result)
    else:
        char = int(char)
        numbers.append(char)

print(*numbers)