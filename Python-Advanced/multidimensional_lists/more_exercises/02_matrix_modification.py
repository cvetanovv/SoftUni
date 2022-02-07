def is_valid(row, col, matrix_size):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True
    return False


matrix_size = int(input())

matrix = []
for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])


while True:
    command_args = input()
    if command_args == "END":
        break
    command_args = command_args.split()
    command, row, col, value = command_args
    row = int(row)
    col = int(col)
    value = int(value)

    if is_valid(row, col, matrix_size):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)