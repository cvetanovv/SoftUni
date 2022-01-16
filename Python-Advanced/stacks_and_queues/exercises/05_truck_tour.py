from collections import deque
n = int(input())

stations = deque()
for _ in range(n):
    pump_data = [int(x) for x in input().split()]
    stations.append(pump_data)

for attempt in range(n):
    tank = 0
    failed = False
    for fuel, distance in stations:
        tank += fuel

        if distance > tank:
            failed = True
            break
        tank -= distance

    if failed:
        stations.append(stations.popleft())
    else:
        print(attempt)
        break
