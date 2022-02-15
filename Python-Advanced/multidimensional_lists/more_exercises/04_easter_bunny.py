def is_inside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


size = int(input())

matrix = []
bunny_position = []

for row_index in range(size):
    row_data = input().split()
    if "B" in row_data:
        bunny_position = [int(row_index), int(row_data.index("B"))]
    matrix.append(row_data)

maximum_eggs = 0
best_direction = ''
bunny_path = []

all_directions = ["up", "down", "left", "right"]

for direction in all_directions:
    eggs = 0
    current_path = []
    bunny_row, bunny_col = bunny_position
    if direction == "up":
        while is_inside(bunny_row - 1, bunny_col, size) and matrix[bunny_row - 1][bunny_col] != "X":
            eggs += int(matrix[bunny_row - 1][bunny_col])
            bunny_row -= 1
            current_path.append([bunny_row, bunny_col])
    elif direction == "down":
        while is_inside(bunny_row + 1, bunny_col, size) and matrix[bunny_row + 1][bunny_col] != "X":
            eggs += int(matrix[bunny_row + 1][bunny_col])
            bunny_row += 1
            current_path.append([bunny_row, bunny_col])
    elif direction == "left":
        while is_inside(bunny_row, bunny_col - 1, size) and matrix[bunny_row][bunny_col - 1] != "X":
            eggs += int(matrix[bunny_row][bunny_col - 1])
            bunny_col -= 1
            current_path.append([bunny_row, bunny_col])
    elif direction == "right":
        while is_inside(bunny_row, bunny_col + 1, size) and matrix[bunny_row][bunny_col + 1] != "X":
            eggs += int(matrix[bunny_row][bunny_col + 1])
            bunny_col += 1
            current_path.append([bunny_row, bunny_col])

    if eggs >= maximum_eggs:
        maximum_eggs = eggs
        best_direction = direction
        bunny_path = current_path

print(best_direction)
for path in bunny_path:
    print(path)
print(maximum_eggs)