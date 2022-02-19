from collections import deque

vowels = deque(input().split())
consonants = input().split()

words = ["rose", "tulip", "lotus", "daffodil"]
letters_found = []

word_is_founded = False

while True:
    if not vowels or not consonants:
        break
    first_letter = vowels.popleft()
    last_letter = consonants.pop()

    for word in words:
        if first_letter in word:
            if first_letter not in letters_found:
                letters_found.append(first_letter)
        if last_letter in word:
            if last_letter not in letters_found:
                letters_found.append(last_letter)

    for word in words:
        has_all = all([char in letters_found for char in word])
        if has_all:
            print(f"Word found: {word}")
            word_is_founded = True
            break
    if word_is_founded:
        break

if not word_is_founded:
    print("Cannot find any word!")

if vowels:
    print("Vowels left:", end=" ")
    print(*vowels)

if consonants:
    print("Consonants left:", end=" ")
    print(*consonants)