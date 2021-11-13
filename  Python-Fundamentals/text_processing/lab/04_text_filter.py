banned_words = input().split(", ")
text = input()

for word in banned_words:
    length_of_banned_words = len(word)
    if word in text:
        text = text.replace(word, "*" * length_of_banned_words)

print(text)