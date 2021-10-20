first_version = [int(num) for num in input().split(".")]


first_version[-1] += 1

if first_version[-1] == 10:
    first_version[-1] = 0
    first_version[-2] += 1
    if first_version[-2] == 10:
        first_version[-2] = 0
        first_version[-3] += 1

new_version = [str(num) for num in first_version]
print(".".join(new_version))