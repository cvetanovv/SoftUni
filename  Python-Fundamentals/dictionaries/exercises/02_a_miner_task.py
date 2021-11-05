resources = {}

while True:
    resource = input()
    if resource == "stop":
        for key, value in resources.items():
            print(f"{key} -> {value}")
        break
    quantity = int(input())

    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity
