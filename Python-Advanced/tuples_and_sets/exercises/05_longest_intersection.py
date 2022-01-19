n = int(input())

longest_intersections = set()

for _ in range(n):
    first_nums = set()
    second_nums = set()
    command = input().split("-")
    first_start, first_end = command[0].split(",")
    first_start = int(first_start)
    first_end = int(first_end)
    for num in range(first_start, first_end + 1):
        first_nums.add(num)

    second_start, second_end = command[1].split(",")
    second_start = int(second_start)
    second_end = int(second_end)
    for num in range(second_start, second_end + 1):
        second_nums.add(num)

    currently_intersections = first_nums.intersection(second_nums)
    if len(currently_intersections) >= len(longest_intersections):
        longest_intersections = currently_intersections

print(f"Longest intersection is [{', '.join([str(num) for num in longest_intersections])}] with length {len(longest_intersections)}")
