rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

sub_matrix = ()
biggest_sum = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        result = matrix[row][column] + matrix[row][column + 1] + matrix[row + 1][column] + matrix[row + 1][column + 1]
        if result > biggest_sum:
            biggest_sum = result
            sub_matrix = (matrix[row][column], matrix[row][column + 1]), (matrix[row + 1][column], matrix[row + 1][column + 1])

for nums in sub_matrix:
    print(*nums)

print(biggest_sum)