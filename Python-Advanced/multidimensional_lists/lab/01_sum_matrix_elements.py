rows, columns = [int(x) for x in input().split(", ")]

matrix = []
result = 0

for i in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)
    result += sum(numbers)

print(result)
print(matrix)
