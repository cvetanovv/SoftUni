list_of_character = input().split(", ")

dic_of_character = {char: ord(char) for char in list_of_character}
print(dic_of_character)