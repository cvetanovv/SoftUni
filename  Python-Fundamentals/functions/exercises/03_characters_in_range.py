def char_in_range(first_char, second_char):
    for num in range(ord(first_char) + 1, ord(second_char)):
        print(chr(num), end=' ')


first_character = input()
second_character = input()

char_in_range(first_character, second_character)