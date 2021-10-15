numbers_as_string = input().split(" ")
numbers = [int(num) for num in numbers_as_string]

filtered_list = filter(lambda num: num % 2 == 0, numbers)
print(list(filtered_list))