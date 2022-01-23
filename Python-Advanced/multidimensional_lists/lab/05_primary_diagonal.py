n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

result = 0

for row in range(n):
    result += matrix[row][row]

print(result)