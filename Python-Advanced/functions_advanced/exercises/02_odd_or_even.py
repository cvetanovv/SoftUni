command = input()
numbers = [int(x) for x in input().split()]

action = 0 if command == "Even" else 1

result = sum([num for num in numbers if num % 2 == action]) * len(numbers)
print(result)
