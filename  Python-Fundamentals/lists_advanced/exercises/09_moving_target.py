targets = [int(num) for num in input().split()]

while True:
    break_check = input()
    if break_check == "End":
        targets_as_string = [str(num) for num in targets]
        print("|".join(targets_as_string))
        break
    command = break_check.split()
    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.remove(targets[index])
    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if index - value >= 0 and index + value <= len(targets) - 1:
            targets = targets[0:index - value] + targets[index + value + 1::]
        else:
            print(f"Strike missed!")
