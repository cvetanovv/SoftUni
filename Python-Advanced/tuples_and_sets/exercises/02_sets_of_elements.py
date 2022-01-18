n, m = [int(num) for num in input().split()]

first_set = set()
second_set = set()

for _ in range(n):
    num = int(input())
    first_set.add(num)

for _ in range(m):
    num = int(input())
    second_set.add(num)

diff_nums = first_set.intersection(second_set)

for num in diff_nums:
    print(num)