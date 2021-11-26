import re

text = input()

numbers = [int(num) for num in re.findall("\d", text)]
threshold = 1
for num in numbers:
    threshold *= num

pattern = r"(::|\*\*)([A-Z][a-z]{2,})(\1)"

matched_emoji = re.finditer(pattern, text)

numbers_of_emoji = 0
coolness_emoji = []

for match in matched_emoji:
    numbers_of_emoji += 1
    ascii_value = sum([ord(letter) for letter in match.group(2)])
    if ascii_value >= threshold:
        coolness_emoji.append(match.group())

print(f"Cool threshold: {threshold}")
print(f"{numbers_of_emoji} emojis found in the text. The cool ones are:")
for emoji in coolness_emoji:
    print(emoji)
