text = input()
encrypted_text = ""

for char in text:
    needed_char_number = ord(char) + 3
    encrypted_text += chr(needed_char_number)

print(encrypted_text)