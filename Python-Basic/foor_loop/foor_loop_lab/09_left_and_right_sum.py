num_of_iterations = int(input())

sum_left_numbers = 0
sum_right_numbers = 0

for x in range(num_of_iterations):
    left_number = int(input())
    sum_left_numbers += left_number

for x in range(num_of_iterations):
    right_number = int(input())
    sum_right_numbers += right_number

diff = abs(sum_right_numbers - sum_left_numbers)

if sum_right_numbers == sum_left_numbers:
    print(f"Yes, sum = {sum_left_numbers}")
else:
    print(f"No, diff = {diff}")