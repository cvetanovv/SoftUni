numbers = [int(num) for num in input().split(", ")]

group = 10

while max(numbers) + 10 > group:
    group_list = []
    for num in numbers:
        if group - 10 < num <= group:
            group_list.append(num)
    print(f"Group of {group}'s: {group_list}")
    group += 10
