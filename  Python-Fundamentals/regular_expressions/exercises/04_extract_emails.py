import re

text = input()
pattern = r"(?<=\s)[a-z0-9]([a-z0-9\._-])+@([a-z]+)[.-]?([a-z]+)[\.-]?([a-z]+)\.([a-z]+)\b"

emails = re.finditer(pattern, text)

for match in emails:
    print(match.group())