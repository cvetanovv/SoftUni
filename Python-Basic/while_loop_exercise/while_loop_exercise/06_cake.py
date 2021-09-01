width_cake = int(input())
height_cake = int(input())

size_cake = width_cake * height_cake

while True:
    piece_cake = input()
    if piece_cake == 'STOP':
        print(f"{size_cake} pieces are left.")
        break
    piece_cake = int(piece_cake)

    size_cake -= piece_cake

    needed_pieces = abs(size_cake)
    if size_cake < 0:
        print(f"No more cake left! You need {needed_pieces} pieces more.")
        break
