num_iterations = int(input())

p1 = 0
p2 = 0
p3 = 0

for x in range(num_iterations):
    numbers = int(input())

    if numbers % 2 == 0:
        p1 += 1
    if numbers % 3 == 0:
        p2 += 1
    if numbers % 4 == 0:
        p3 += 1

p1 = (p1 / num_iterations) * 100
p2 = (p2 / num_iterations) * 100
p3 = (p3 / num_iterations) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")