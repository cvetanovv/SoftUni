number = int(input())

counter = 0

for num1 in range(number + 1):
    for num2 in range(number + 1):
        for num3 in range(number + 1):
            if num1 + num2 + num3 == number:
                counter += 1

print(counter)