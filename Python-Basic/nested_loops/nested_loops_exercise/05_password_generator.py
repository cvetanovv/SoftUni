n = int(input())
l = int(input())

for num_one in range(1, n + 1):
    for num_two in range(1, n + 1):
        for num_three in range(97, 97 + l):
            for num_four in range(97, 97 + l):
                for num_five in range(1, n + 1):
                    if num_five > num_one and num_five > num_two:
                        print(f"{num_one}{num_two}{chr(num_three)}{chr(num_four)}{num_five}", end=' ')
