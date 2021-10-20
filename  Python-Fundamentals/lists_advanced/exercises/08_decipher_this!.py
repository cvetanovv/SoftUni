secret_words = input().split()

words = []

for secret_word in secret_words:
    secret_word_only_alphabet = [letter for letter in secret_word if not letter.isdigit()]
    digits = ''
    for letter in secret_word:
        if letter.isdigit():
            digits += letter
    digits = int(digits)
    final_word = []
    first_letter = chr(digits)
    final_word.append(first_letter)
    final_word += secret_word_only_alphabet
    final_word[1], final_word[-1] = final_word[-1], final_word[1]
    final_word_as_string = "".join(final_word)
    words.append(final_word_as_string)

print(" ".join(words))

