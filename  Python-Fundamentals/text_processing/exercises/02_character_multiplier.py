strings = input().split()
first_string = strings[0]
second_string = strings[1]

slice_counter = 0
result = 0

if len(first_string) == len(second_string):
    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])
elif len(first_string) < len(second_string):
    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])
        slice_counter += 1
    for char in second_string[slice_counter:]:
        result += ord(char)
elif len(first_string) > len(second_string):
    for index in range(len(second_string)):
        result += ord(first_string[index]) * ord(second_string[index])
        slice_counter += 1
    for char in first_string[slice_counter:]:
        result += ord(char)

print(result)