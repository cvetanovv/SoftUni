import sys

num_of_iterrations = int(input())

max_num = -sys.maxsize
min_num = sys.maxsize

for x in range(num_of_iterrations):
    number = int(input())
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
