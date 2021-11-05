string = input().replace(" ", "")

chars_in_dic = {}

for char in string:
    if char not in chars_in_dic:
        chars_in_dic[char] = 1
    else:
        chars_in_dic[char] += 1

for key, value in chars_in_dic.items():
    print(f"{key} -> {value}")