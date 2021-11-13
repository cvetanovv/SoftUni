text = input().split()
result = ""

for word in text:
    word_length = len((word))
    result += word * word_length

print(result)