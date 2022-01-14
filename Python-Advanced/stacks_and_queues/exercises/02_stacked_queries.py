n = int(input())
stacked_numbers = []

for _ in range(n):
    queries = input().split()
    command = queries[0]
    if command == "1":
        number = int(queries[1])
        stacked_numbers.append(number)
    elif command == "2":
        if stacked_numbers:
            stacked_numbers.pop()
    elif command == "3":
        print(max(stacked_numbers))
    elif command == "4":
        print(min(stacked_numbers))

reversed_stacked_numbers = []
while stacked_numbers:
    num = stacked_numbers.pop()
    reversed_stacked_numbers.append(num)

stacked_numbers_as_string = [str(num) for num in reversed_stacked_numbers]
print(f", ".join(stacked_numbers_as_string))