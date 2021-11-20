import re

text = input().lower()
needed_word = input().lower()
pattern = fr"\b{needed_word}\b"

matched = re.findall(pattern, text)

print(len(matched))