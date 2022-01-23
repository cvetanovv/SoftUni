n = int(input())

matrix = []

for _ in range(n):
    symbols = input()
    matrix.append([char for char in symbols])

needed_symbol = input()

for row_index in range(n):
    for column_index in range(len(matrix)):
        if matrix[row_index][column_index] == needed_symbol:
            position = matrix[row_index][column_index]
            print(f"({row_index}, {column_index})")
            exit()

print(f"{needed_symbol} does not occur in the matrix")