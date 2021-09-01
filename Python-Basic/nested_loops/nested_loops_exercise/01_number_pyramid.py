number = int(input())

current = 1
its_current_bigger_that_number = False

for row in range(1, number + 1):
    for column in range(1, row + 1):

        if current > number:
            its_current_bigger_that_number = True
            break
        print(f"{current}", end=' ')
        current += 1

    if its_current_bigger_that_number:
        break
    print()