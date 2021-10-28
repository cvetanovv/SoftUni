bakery_list = input().split()

bakery_dict = {}

for i in range(0, len(bakery_list), 2):
    bakery_dict[bakery_list[i]] = int(bakery_list[i + 1])

print(bakery_dict)