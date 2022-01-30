from collections import deque

working_bees = deque(int(x) for x in input().split())
nectars = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

while True:
    if not working_bees or not nectars:
        break
    bee = working_bees.popleft()
    nectar = nectars.pop()
    if nectar < bee:
        working_bees.appendleft(bee)
        continue

    symbol = symbols.popleft()
    if symbol == "+":
        result = bee + nectar
        total_honey += abs(result)
    elif symbol == "-":
        result = bee - nectar
        total_honey += abs(result)
    elif symbol == "*":
        result = bee * nectar
        total_honey += abs(result)
    elif symbol == "/":
        if bee != 0 and nectar != 0:
            result = bee / nectar
            total_honey += abs(result)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")