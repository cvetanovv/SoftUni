floors = int(input())
rooms = int(input())

for floor in range(floors, 0, - 1):
    for room in range(0, rooms):

        if floor % 2 == 0:
            if floor == floors:
                print(f"L{floor}{room}", end=' ')
            else:
                print(f"O{floor}{room}", end=' ')
        if floor % 2 == 1:
            if floor == floors:
                print(f"L{floor}{room}", end=' ')
            else:
                print(f"A{floor}{room}", end=' ')

    print()
