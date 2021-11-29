import re

text = input()

pattern = r"(@|#)(?P<word_one>[A-Za-z]{3,})(\1)(\1)(?P<word_two>[A-Za-z]{3,})(\1)"

matched_word = re.finditer(pattern,text)
match_len = 0
mirror_words = []

for match in matched_word:
    match_len += 1
    words_dict = match.groupdict("word_one")
    first_word = words_dict["word_one"]
    second_word = words_dict["word_two"]
    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")

if match_len == 0:
    print("No word pairs found!")
else:
    print(f"{match_len} word pairs found!")

if mirror_words:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print(f"No mirror words!")