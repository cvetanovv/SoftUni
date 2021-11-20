import string

list_of_strings = [text.strip() for text in input().split()]
total_sum = 0

for text in list_of_strings:
    number = ""
    temporary_sum = 0
    for num in text:
        if num.isdigit():
            number += num
    if text[0].isupper():
        temporary_sum += (int(number) / (string.ascii_uppercase.index(text[0]) + 1))
    elif text[0].islower():
        temporary_sum += (int(number) * (string.ascii_lowercase.index(text[0]) + 1))
    if text[-1].isupper():
        temporary_sum -= (string.ascii_uppercase.index(text[-1]) + 1)
    elif text[-1].islower():
        temporary_sum += (string.ascii_lowercase.index(text[-1]) + 1)
    total_sum += temporary_sum

print(f"{total_sum:.2f}")
