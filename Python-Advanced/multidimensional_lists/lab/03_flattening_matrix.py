number_of_rows = int(input())

matrix = []

for i in range(number_of_rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.extend(numbers)

print(matrix)