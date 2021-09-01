num_iterrations = int(input())

all_nums = 0
for num in range(num_iterrations):
    number = int(input())
    all_nums += number

print(f"{all_nums / num_iterrations:.2f}")