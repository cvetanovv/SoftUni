def concatenate(*words):
    sentence = ""
    for word in words:
        sentence += word
    return sentence


print(concatenate("Soft", "Uni", "Is", "Great", "!"))