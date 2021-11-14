text = input()

emoticons = []

for index in range(len(text)):
    emoticon = ":"
    if text[index] == ":":
        emoticon += text[index + 1]
        emoticons.append(emoticon)

for emoji in emoticons:
    print(emoji)