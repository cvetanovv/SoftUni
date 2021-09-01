num_iterations = int(input())

result = 0
from0_to9 = 0
from10_to19 = 0
from20_to29 = 0
from30_to39 = 0
from40_to50 = 0
invalid = 0

for num in range(num_iterations):
    number = int(input())

    if 0 <= number <= 9:
        result += number * 0.20
        from0_to9 += 1
    elif 10 <= number <= 19:
        result += number * 0.30
        from10_to19 += 1
    elif 20 <= number <= 29:
        result += number * 0.40
        from20_to29 += 1
    elif 30 <= number <= 39:
        result += 50
        from30_to39 += 1
    elif 40 <= number <= 50:
        result += 100
        from40_to50 += 1
    elif number > 50 or number < 0:
        result /= 2
        invalid += 1

from0_to9_percent = from0_to9 / num_iterations * 100
from10_to19_percent = from10_to19 / num_iterations * 100
from20_to29_percent = from20_to29 / num_iterations * 100
from30_to39_percent = from30_to39 / num_iterations * 100
from40_to50_percent = from40_to50 / num_iterations * 100
invalid_percent = invalid / num_iterations * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {from0_to9_percent:.2f}%")
print(f"From 10 to 19: {from10_to19_percent:.2f}%")
print(f"From 20 to 29: {from20_to29_percent:.2f}%")
print(f"From 30 to 39: {from30_to39_percent:.2f}%")
print(f"From 40 to 50: {from40_to50_percent:.2f}%")
print(f"Invalid numbers: {invalid_percent:.2f}%")