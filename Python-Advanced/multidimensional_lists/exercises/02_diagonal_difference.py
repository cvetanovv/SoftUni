n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(num) for num in input().split()])

primary_sum = 0
secondary_sum = 0

for row in range(n):
    primary_sum += matrix[row][row]
    secondary_sum += matrix[row][n - 1 - row]

print(abs(primary_sum - secondary_sum))