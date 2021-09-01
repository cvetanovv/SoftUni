
steps_counter = 0

while True:
    steps = input()
    if steps == 'Going home':
        last_steps = int(input())
        steps_counter += last_steps
        diff = abs(steps_counter - 10000)
        if steps_counter >= 10000:
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break
        else:
            print(f"{diff} more steps to reach goal.")
            break

    steps = int(steps)
    steps_counter += steps
    if steps_counter >= 10000:
        diff = abs(steps_counter - 10000)
        print("Goal reached! Good job!")
        print(f"{diff} steps over the goal!")
        break

