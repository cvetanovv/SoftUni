n = int(input())

odd_nums = set()
even_nums = set()

for row in range(1, n + 1):
    sum_name = sum([ord(char) for char in input()]) // row

    if sum_name % 2 == 0:
        even_nums.add(sum_name)
    else:
        odd_nums.add(sum_name)

if sum(odd_nums) == sum(even_nums):
    union_set = odd_nums.union(even_nums)
    print(f"{', '.join(str(num) for num in union_set)}")
elif sum(odd_nums) > sum(even_nums):
    different_values = odd_nums.difference(even_nums)
    print(f"{', '.join(str(num) for num in different_values)}")
elif sum(odd_nums) < sum(even_nums):
    symmetric_diff_values = even_nums.symmetric_difference(odd_nums)
    print(f"{', '.join(str(num) for num in symmetric_diff_values)}")
