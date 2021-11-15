string = input()

result = ''
explosion = 0

for index in range(len(string)):
    if explosion != 0:
        explosion -= 1
        continue
    if string[index] == ">":
        explosion += int(string[index + 1])
        result += ">"
        if string[index + 2] == ">":
            explosion += int(string[index + 3]) + 1
            result += ">"
    else:
        result += string[index]

print(result)