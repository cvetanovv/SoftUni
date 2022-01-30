from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while True:
    if milkshakes == 5 or not chocolates or not cups_of_milk:
        break
    chocolate = chocolates.pop()
    milk = cups_of_milk.popleft()
    if milk <= 0:
        chocolates.append(chocolate)
        continue
    if chocolate <= 0:
        cups_of_milk.appendleft(milk)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        cups_of_milk.append(milk)
        chocolate -= 5
        chocolates.append(chocolate)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")