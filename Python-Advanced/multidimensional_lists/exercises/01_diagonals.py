n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])


primary_diagonal = []
secondary_diagonal = []

for row in range(n):
    primary_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][len(matrix[row]) - 1 - row])

print(f"Primary diagonal: {', '.join(str(num) for num in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(num) for num in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")