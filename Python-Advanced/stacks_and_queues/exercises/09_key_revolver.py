from collections import deque

price_of_each_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(num) for num in input().split()]
locks = deque(int(num) for num in input().split())
intelligence = int(input())

gun_size = size_of_gun_barrel
reloading_counter = 0
fired_bullets = 0

while True:
    if gun_size == 0 and bullets:
        gun_size = size_of_gun_barrel
        reloading_counter += 1
        print("Reloading!")
    if not locks:
        bullets_cost = fired_bullets * price_of_each_bullet
        print(f"{len(bullets)} bullets left. Earned ${intelligence - bullets_cost}" )
        break
    if not bullets:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    bullets_to_shot = bullets.pop()
    if bullets_to_shot <= locks[0]:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")
    gun_size -= 1
    fired_bullets += 1
