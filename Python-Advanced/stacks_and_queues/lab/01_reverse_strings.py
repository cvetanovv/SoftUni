text = list(input())

for index in range(len(text) - 1, -1, -1):
    print(text.pop(index), end='')