string = input()

digits = ""
letters = ""
characters = ""

for letter in string:
    if letter.isdigit():
        digits += letter
    elif letter.isalpha():
        letters += letter
    else:
        characters += letter

print(digits)
print(letters)
print(characters)
