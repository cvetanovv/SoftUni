text = input()

char_dict = {}

for char in text:
    if char not in char_dict:
        char_dict[char] = 0
    char_dict[char] += 1

for char, count in sorted(char_dict.items()):
    print(f"{char}: {count} time/s")