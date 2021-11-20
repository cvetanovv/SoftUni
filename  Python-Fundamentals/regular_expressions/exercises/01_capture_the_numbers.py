import re

text = input()
pattern = r"\d+"
numbers = []

while text:
    match_numbers = re.findall(pattern, text)
    if match_numbers:
        numbers += match_numbers

    text = input()

print(*numbers)