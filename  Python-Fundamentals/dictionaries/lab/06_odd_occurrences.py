list_of_elements = input().lower().split()

dic_of_elements = {}

for element in list_of_elements:
    if element in list_of_elements:
        dic_of_elements[element] = 0

for element in list_of_elements:
    dic_of_elements[element] += 1

filtered_list = []

for key, value in dic_of_elements.items():
    if value % 2 != 0:
        filtered_list.append(key)

print(" ".join(filtered_list))
