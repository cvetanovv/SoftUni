rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(num) for num in input().split()])

sub_matrix = []
sum_sub_matrix = -99999999999999999

for row in range(rows - 2):
    for column in range(columns - 2):
        current_square = matrix[row][column] + matrix[row][column + 1] + matrix[row][column + 2] \
                         + matrix[row + 1][column] + matrix[row + 1][column + 1] + matrix[row + 1][column + 2] \
                         + matrix[row + 2][column] + matrix[row + 2][column + 1] + matrix[row + 2][column + 2]
        if current_square >= sum_sub_matrix:
            sum_sub_matrix = current_square
            sub_matrix = [[matrix[row][column], matrix[row][column + 1], matrix[row][column + 2]],
                  [matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2]],
                  [matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]]

print(f"Sum = {sum_sub_matrix}")
for nums in sub_matrix:
    print(*nums)
