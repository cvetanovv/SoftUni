divisor_number = int(input())
boundary_number = int(input())

correct_number = 0
for number in range(boundary_number + 1):
    if number % divisor_number == 0:
        if number > correct_number:
            correct_number = number

print(correct_number)