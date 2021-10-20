rooms = int(input())

all_chairs = 0
all_visitors = 0

for i in range(1, rooms + 1):
    room = input().split()
    chairs = room[0]
    visitors = int(room[1])
    all_chairs += len(chairs)
    all_visitors += visitors

    if visitors > len(chairs):
        print(f"{visitors - len(chairs)} more chairs needed in room {i}")

chair_left = all_chairs - all_visitors
if chair_left >= 0:
    print(f"Game On, {chair_left} free chairs left")