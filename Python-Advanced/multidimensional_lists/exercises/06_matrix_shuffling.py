def is_inside(row1, col1, row2, col2):
    if row1 < 0 or row1 > rows or row2 < 0 or row2 > rows \
            or col1 < 0 or col1 > columns or col2 < 0 or col2 > columns:
        return False
    return True


rows, columns = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input().split()
    if command[0] == "END":
        break
    elif command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue
    else:
        row1, col1, row2, col2 = ([int(x) for x in command[1:]])
        if not is_inside(row1, col1, row2, col2):
            print("Invalid input!")
        else:
            swap_num = matrix[row1][col1]
            matrix[row1][col1] = matrix[row2][col2]
            matrix[row2][col2] = swap_num
            for row in matrix:
                print(*row)
