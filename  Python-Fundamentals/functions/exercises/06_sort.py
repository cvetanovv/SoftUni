numbers_as_string = input().split(" ")
numbers = [int(num) for num in numbers_as_string]
print(sorted(numbers))