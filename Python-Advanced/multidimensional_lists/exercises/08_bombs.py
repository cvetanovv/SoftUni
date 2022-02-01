def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbours(row, col, matrix):
    size = len(matrix)
    neighbours = []
    if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbours.append([row - 1, col])
    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbours.append([row + 1, col])
    if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbours.append([row, col - 1])
    if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbours.append([row, col + 1])
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbours.append([row - 1, col - 1])
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbours.append([row - 1, col + 1])
    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbours.append([row + 1, col - 1])
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbours.append([row + 1, col + 1])
    return neighbours


matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    matrix.append([int(num) for num in input().split()])

coordinates = input().split()


for bomb_coord in coordinates:
    bomb_row, bomb_col = [int(x) for x in bomb_coord.split(",")]
    if matrix[bomb_row][bomb_col] <= 0:
        continue
    bomb_power = matrix[bomb_row][bomb_col]
    neighbours = get_neighbours(bomb_row, bomb_col, matrix)
    matrix[bomb_row][bomb_col] = 0

    for row, col in neighbours:
        matrix[row][col] -= bomb_power

alive_cell = 0
alive_cells_sum = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cell += 1
            alive_cells_sum += el

print(f"Alive cells: {alive_cell}")
print(f"Sum: {alive_cells_sum}")

for row in matrix:
    print(*row)