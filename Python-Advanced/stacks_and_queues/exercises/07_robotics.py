from collections import deque

def conv_str_to_seconds(str_time):
    hours, minutes, seconds = [int(x) for x in str_time.split(":")]
    return hours * 60 * 60 + minutes * 60 + seconds


robots_data = input().split(";")
time = conv_str_to_seconds(input())
process_time_by_robot = {}
busy_time_by_robot = {}

for robot in robots_data:
    name, process_time = robot.split("-")
    process_time = int(process_time)
    process_time_by_robot[name] = process_time
    busy_time_by_robot[name] = -1

items = deque()
while True:
    item = input()
    if item == "End":
        break
    items.append(item)


def conv_sec_to_str_time(seconds):
    seconds %= 24 * 60 * 60
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


while items:
    time += 1
    item = items.popleft()
    for name, busy_until in busy_time_by_robot.items():
        if time >= busy_until:
            print(f"{name} - {item} [{conv_sec_to_str_time(time)}]")
            busy_time_by_robot[name] = time + process_time_by_robot[name]
            break
    else:
        items.append(item)
