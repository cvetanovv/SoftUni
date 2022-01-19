from collections import deque

first_nums = set([int(num) for num in input().split()])
second_nums = set([int(num) for num in input().split()])
number_of_iterations = int(input())

for _ in range(number_of_iterations):
    command = deque(input().split())
    main_action = command.popleft()
    second_action = command.popleft()

    if main_action == "Add":
        numbers = set([int(num) for num in command])
        if second_action == "First":
            first_nums.update(numbers)
        elif second_action == "Second":
            second_nums.update(numbers)
    elif main_action == "Remove":
        numbers = set([int(num) for num in command])
        if second_action == "First":
            first_nums.difference_update(numbers)
        elif second_action == "Second":
            second_nums.difference_update(numbers)
    else:
        if first_nums.issubset(second_nums) or second_nums.issubset(first_nums):
            print("True")
        else:
            print("False")


print(", ".join(str(num) for num in sorted(first_nums)))
print(", ".join(str(num) for num in sorted(second_nums)))