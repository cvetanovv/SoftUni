
saved_sum = 0

while True:
    destination = input()
    if destination == 'End':
        break
    sum_need_for_trip = float(input())

    while True:
        add_sum = float(input())
        saved_sum += add_sum
        if saved_sum >= sum_need_for_trip:
            print(f"Going to {destination}!")
            saved_sum = 0
            break
