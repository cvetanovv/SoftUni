import sys
num_iterations = int(input())

sum = 0
biggest = -sys.maxsize
for x in range(num_iterations):
    numbers = int(input())
    sum += numbers
    if numbers > biggest:
        biggest = numbers

sum -= biggest
diff = abs(sum - biggest)

if sum == biggest:
    print('Yes')
    print(f'Sum = {sum}')
else:
    print('No')
    print(f"Diff = {diff}")