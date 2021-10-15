numbers_as_string = input().split(" ")
numbers = [int(number) for number in numbers_as_string]

print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"The sum number is: {sum(numbers)}")