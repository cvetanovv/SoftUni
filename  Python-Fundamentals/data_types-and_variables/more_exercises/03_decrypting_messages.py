key = int(input())
num_of_iterations = int(input())

text = ''
for i in range(num_of_iterations):
    letter = input()
    new_letter = chr(ord(letter) + key)
    text += new_letter

print(text)