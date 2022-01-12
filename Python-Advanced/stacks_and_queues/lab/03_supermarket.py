from collections import deque

line = deque()

name = input()

while name != "End":
    if name == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(name)
    name = input()

print(f"{len(line)} people remaining.")