def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def white_move(row, col):
    return row - 1, col


def black_move(row, col):
    return row + 1, col


def black_enemy(row, col, size, matrix):
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] == matrix[black_row][black_col]:
        return True
    if is_inside(row - 1, col, size) and matrix[row - 1][col] == matrix[black_row][black_col]:
        return True
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] == matrix[black_row][black_col]:
        return True


def white_enemy(row, col, size, matrix):
    if is_inside(row - 1, col - 1, size) and matrix[row + 1][col + 1] == matrix[white_row][white_col]:
        return True
    if is_inside(row - 1, col, size) and matrix[row + 1][col] == matrix[white_row][white_col]:
        return True
    if is_inside(row - 1, col + 1, size) and matrix[row + 1][col - 1] == matrix[white_row][white_col]:
        return True


size = 8

matrix = []

for _ in range(size):
    matrix.append(input().split())

white_row = 0
white_col = 0
black_row = 0
black_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "w":
            white_row = row
            white_col = col
        if matrix[row][col] == "b":
            black_row = row
            black_col = col

letter_counter = 0
num_counter = 8
for row in range(size):
    for col in range(size):
        matrix[row][col] = f"{chr(97 + letter_counter)}{num_counter}"
        letter_counter += 1
    letter_counter = 0
    num_counter -= 1

matrix[white_row][white_col] = "w"
matrix[black_row][black_col] = "b"
a = 5
while True:
    if black_enemy(white_row, white_col, size, matrix):
        print(f"Game over! White win, capture on {matrix[black_row][black_col]}.")
        break
    white_row, white_col = white_move(white_row, white_col)
    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {matrix[white_row][white_col]}.")
        break
    # matrix[white_row][white_col] = "w"


    if white_enemy(black_row, black_col, size, matrix):
        print(f"Game over! Black win, capture on {matrix[white_row][white_col]}.")
        break
    black_row += 1
    if black_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {matrix[black_row][black_col]}.")
        break
    # matrix[white_row][white_col] = "a"
