def get_next_pos(command, row, col):
    if command == "up":
        return row - 1, col
    if command == "left":
        return row, col - 1
    if command == "right":
        return row, col + 1
    if command == "down":
        return row + 1, col


matrix_size = int(input())
commands = input().split()

matrix = []

for _ in range(matrix_size):
    matrix.append(input().split())

miner_row = 0
miner_col = 0
total_col = 0

for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == "s":
            miner_row = row
            miner_col = col
        if matrix[row][col] == "c":
            total_col += 1

game_over = False
for command in commands:
    next_row, next_col = get_next_pos(command, miner_row, miner_col)

    if next_row < 0 or next_row >= matrix_size or next_col < 0 or next_col >= matrix_size:
        continue

    miner_row, miner_col = next_row, next_col
    if matrix[miner_row][miner_col] == "c":
        matrix[miner_row][miner_col] = "*"
        total_col -= 1

        if total_col == 0:
            break
    elif matrix[miner_row][miner_col] == "e":
        game_over = True
        break

if total_col == 0:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif game_over:
    print(f"Game over! ({miner_row}, {miner_col})")
else:
    print(f"{total_col} pieces of coal left. ({miner_row}, {miner_col})")