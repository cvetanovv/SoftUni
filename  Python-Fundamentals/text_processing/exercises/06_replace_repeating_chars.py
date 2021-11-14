text = input()

index = 0
result = f""

while index < len(text) - 1:
    if text[index] == text[index + 1]:
        index += 1
        continue
    else:
        result += text[index]
        index += 1

print(result + f"{text[-1]}")