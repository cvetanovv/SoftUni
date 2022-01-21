rows = int(input())

matrix = []

for i in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)

even_numbers = [[num for num in matrix[i] if num % 2 == 0]for i in range(len(matrix))]
print(even_numbers)