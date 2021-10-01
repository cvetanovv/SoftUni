number_of_iterations = int(input())
word = input()
text_list = []

for i in range(number_of_iterations):
    text = input()
    text_list.append(text)
print(text_list)

filtered_list = []
for string in text_list:
    if word in string:
        filtered_list.append(string)
print(filtered_list)