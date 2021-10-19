text = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'i']
final_text = [letter for letter in text if letter not in vowels]
print("".join(final_text))