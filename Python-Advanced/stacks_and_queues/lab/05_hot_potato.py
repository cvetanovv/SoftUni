from collections import deque

kids = deque(input().split(" "))
n = int(input())

while len(kids) > 1:
    kids.rotate(-n)
    removed_kid = kids.pop()
    print(f"Removed {removed_kid}")

print(f"Last is {kids.popleft()}")