num_of_iterations = int(input())

odd_nums = 0
even_nums = 0

for x in range(num_of_iterations):
    number = int(input())
    if x % 2 == 0:
        even_nums += number
    else:
        odd_nums += number

diff = abs(odd_nums - even_nums)

if odd_nums == even_nums:
    print('Yes')
    print(f"Sum = {odd_nums}")
else:
    print('No')
    print(f"Diff = {diff}")