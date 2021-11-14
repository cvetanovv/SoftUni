string = input().split("\\")
needed_text = string[-1].split(".")

print(f"File name: {needed_text[0]}")
print(f"File extension: {needed_text[1]}")