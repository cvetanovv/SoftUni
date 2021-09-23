first_string = input()
second_string = input()

first_string_list = ','.join(first_string).split(',')
second_string_list = ','.join(second_string).split(',')

for index in range(len(first_string)):
    if first_string_list[index] == second_string_list[index]:
        continue
    else:
        first_string_list[index] = second_string_list[index]
        print(''.join(first_string_list))