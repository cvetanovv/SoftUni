num_iterations = int(input())

numbers = []

for x in range(num_iterations):
    first_number = int(input())
    second_number = int(input())

    numbers.append(first_number + second_number)

max_num = max(numbers)
min_num = min(numbers)


if max_num == min_num:
    print(f"Yes, value={max_num}")
else:
    diff = abs(numbers[-1] - numbers[-2])
    print(f"No, maxdiff={diff}")