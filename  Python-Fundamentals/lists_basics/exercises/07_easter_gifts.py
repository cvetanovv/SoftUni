gifts = input().split()

while True:
    command = input().split()
    gift = command[1]
    gifts_length = len(gifts)
    if command[0] == "OutOfStock":
        for i in range(gifts_length):
            if gifts[i] == gift:
                gifts[i] = 'None'
    elif command[0] == "Required":
        replace_index = command[2]
        replace_index = int(replace_index)
        if 0 <= replace_index < gifts_length:
            gifts[replace_index] = gift
    elif command[0] == "JustInCase":
        gifts.pop()
        gifts.append(gift)
    command_for_break = ' '.join(command)
    if command_for_break == "No Money":
        break

for gift in gifts:
    if gift == 'None':
        continue
    else:
        print(gift, end=' ')