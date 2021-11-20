import re

pattern = r"\s_([A-Za-z]+\b)"
text = input()

matched_word = re.findall(pattern, text)

print(",".join(matched_word))