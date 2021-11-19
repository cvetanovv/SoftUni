import re

pattern = r"\b[A-Z][a-z]+\b \b[A-Z][a-z]+\b"
text = input()

name = re.findall(pattern, text)

print(*name)