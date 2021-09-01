num_iterations = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for x in range(num_iterations):
    number = int(input())
    if number < 200:
        p1 += 1
    elif 200 <= number < 400:
        p2 += 1
    elif 400 <= number < 600:
        p3 += 1
    elif 600 <= number < 800:
        p4 += 1
    elif number >= 800:
        p5 += 1

p1 = (p1 / num_iterations) * 100
p2 = (p2 / num_iterations) * 100
p3 = (p3 / num_iterations) * 100
p4 = (p4 / num_iterations) * 100
p5 = (p5 / num_iterations) * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")