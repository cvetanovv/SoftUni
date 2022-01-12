expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == "(":
        stack.append(index)
    if expression[index] == ")":
        start_index = stack.pop()
        print(expression[start_index:index + 1])