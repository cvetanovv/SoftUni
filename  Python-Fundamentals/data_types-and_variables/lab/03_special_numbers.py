numbers_of_iteration = int(input())

for number in range(1, numbers_of_iteration + 1):
    if number < 10:
        if number == 5 or number == 7:
            print(f"{number} -> True")
        else:
            print(f"{number} -> False")
    else:
        number = str(number)
        counter = 0
        for num in number:
            num = int(num)
            counter += num
        if counter == 5 or counter == 7:
            print(f"{number} -> True")
        else:
            print(f"{number} -> False")