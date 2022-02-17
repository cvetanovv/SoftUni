def is_inside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


size = int(input())

matrix = []
alice_position = []
bags_of_tea = 0

for row_index in range(size):
    row_data = input().split()
    if "A" in row_data:
        alice_position = [int(row_index), int(row_data.index("A"))]
    matrix.append(row_data)

is_success = True

while True:
    command = input()
    alice_row, alice_col = alice_position
    matrix[alice_row][alice_col] = "*"
    if command == "down":
        if is_inside(alice_row + 1, alice_col, size):
            if matrix[alice_row + 1][alice_col] == "R":
                matrix[alice_row + 1][alice_col] = "*"
                is_success = False
                break
            elif matrix[alice_row + 1][alice_col] == ".":
                alice_position = [alice_row + 1, alice_col]
            elif matrix[alice_row + 1][alice_col] == "*":
                alice_position = [alice_row + 1, alice_col]
            else:
                bags_of_tea += int(matrix[alice_row + 1][alice_col])
                alice_position = [alice_row + 1, alice_col]
        else:
            is_success = False
            break
    elif command == "up":
        if is_inside(alice_row - 1, alice_col, size):
            if matrix[alice_row - 1][alice_col] == "R":
                matrix[alice_row - 1][alice_col] = "*"
                is_success = False
                break
            elif matrix[alice_row - 1][alice_col] == ".":
                alice_position = [alice_row - 1, alice_col]
            elif matrix[alice_row - 1][alice_col] == "*":
                alice_position = [alice_row - 1, alice_col]
            else:
                bags_of_tea += int(matrix[alice_row - 1][alice_col])
                alice_position = [alice_row - 1, alice_col]
        else:
            is_success = False
            break
    elif command == "left":
        if is_inside(alice_row, alice_col - 1, size):
            if matrix[alice_row][alice_col - 1] == "R":
                matrix[alice_row][alice_col - 1] = "*"
                is_success = False
                break
            elif matrix[alice_row][alice_col - 1] == ".":
                alice_position = [alice_row, alice_col - 1]
            elif matrix[alice_row][alice_col - 1] == "*":
                alice_position = [alice_row, alice_col - 1]
            else:
                bags_of_tea += int(matrix[alice_row][alice_col - 1])
                alice_position = [alice_row, alice_col - 1]
        else:
            is_success = False
            break
    elif command == "right":
        if is_inside(alice_row, alice_col + 1, size):
            if matrix[alice_row][alice_col + 1] == "R":
                matrix[alice_row][alice_col + 1] = "*"
                is_success = False
                break
            elif matrix[alice_row][alice_col + 1] == ".":
                alice_position = [alice_row, alice_col + 1]
            elif matrix[alice_row][alice_col + 1] == "*":
                alice_position = [alice_row, alice_col + 1]
            else:
                bags_of_tea += int(matrix[alice_row][alice_col + 1])
                alice_position = [alice_row, alice_col + 1]
        else:
            is_success = False
            break
    if bags_of_tea >= 10:
        matrix[alice_row][alice_col + 1] = "*"
        break


if is_success:
    print("She did it! She went to the party.")
    for row in matrix:
        print(*row)
else:
    print("Alice didn't make it to the tea party.")

    for row in matrix:
        print(*row)
