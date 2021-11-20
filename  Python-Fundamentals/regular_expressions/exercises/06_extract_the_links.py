import re

pattern = r"www.[a-zA-Z0-9-]+(\.[a-z]*)*\.[a-z]+"
command = input()

while command:
    match = re.finditer(pattern, command)
    if match:
        for email in match:
            print(email.group())
    command = input()