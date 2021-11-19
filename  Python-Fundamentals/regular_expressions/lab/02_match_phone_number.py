import re

pattern = r"\+359([\s-])2(\1)\d{3}(\1)\d{4}\b"
text = input()

tel_numbers = re.finditer(pattern, text)
matched_numbers = []

for number in tel_numbers:
    matched_numbers.append(number.group())

print(", ".join(matched_numbers))