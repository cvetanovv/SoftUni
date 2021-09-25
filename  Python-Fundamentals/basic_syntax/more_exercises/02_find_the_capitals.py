text = input()

capital_letters_indices = []

for index in range(len(text)):
    if text[index].isupper():
        capital_letters_indices.append(index)

print(capital_letters_indices)