from collections import deque

green_light = int(input())
duration_free_window = int(input())

duration_green_light = green_light
time_to_pass = 0

cars = deque()
passed_car = 0

while True:
    car = input()
    if car == "END":
        break
    elif car == "green":
        while cars:
            first_car = cars.popleft()
            len_first_car = len(first_car)
            if duration_green_light > 0:
                if duration_green_light - len_first_car > 0:
                    duration_green_light -= len_first_car
                    passed_car += 1
                else:
                    time_to_pass = duration_green_light + duration_free_window
                    if time_to_pass - len_first_car < 0:
                        character_hit = first_car[time_to_pass]
                        print("A crash happened!")
                        print(f"{first_car} was hit at {character_hit}.")
                        exit()
                    else:
                        passed_car += 1
                        break
        duration_green_light = green_light
    else:
        cars.append(car)

print("Everyone is safe.")
print(f"{passed_car} total cars passed the crossroads.")
