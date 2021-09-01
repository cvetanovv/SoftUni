max_first_num = int(input())
max_second_num = int(input())
max_thirth_num = int(input())

for num_one in range(1, max_first_num + 1):
    for num_two in range(2, max_second_num + 1):
        for num_three in range(1, max_thirth_num + 1):
            if num_three % 2 == 0 and num_one % 2 == 0 and (
                    num_two == 2 or num_two == 3 or num_two == 5 or num_two == 7) and num_two <= max_second_num:
                print(f"{num_one} {num_two} {num_three}")