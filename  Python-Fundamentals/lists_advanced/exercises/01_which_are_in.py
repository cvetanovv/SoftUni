first_list = input().split(", ")
second_list = input().split(", ")

final_list = []

for word in first_list:
    for second_word in second_list:
        if word in second_word and word not in final_list:
            final_list.append(word)

print(final_list)

