rows, cols = [int(x) for x in input().split()]
word = input()

matrix = []
word_idx = 0

for row in range(rows):
    matrix.append([None] * cols)
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = word[word_idx]
        else:
            matrix[row][cols - 1 - col] = word[word_idx]
        word_idx = (word_idx + 1) % len(word)

for word in matrix:
    new_word = ""
    for char in word:
        new_word += char
    print(new_word)