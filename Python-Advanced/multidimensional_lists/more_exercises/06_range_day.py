def take_next_steps(row_, col_, steps__, action_):
    if action_ == "up":
        return row_ - steps__, col_
    elif action_ == "down":
        return row_ + steps__, col_
    elif action_ == "left":
        return row_, col_ - steps__
    elif action_ == "right":
        return row_, col_ + steps__


def is_outside(row__, col__, m_size__):
    return row__ < 0 or col__ < 0 or row__ >= m_size__ or col__ >= m_size__


m_size = 5
matrix, target_coords = [], []
player_row, player_col = 0, 0
total_targets = 0

hit_targets = 0
for row_el in range(m_size):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col_el in range(len(row_elements)):
        if row_elements[col_el] == "A":
            player_row, player_col = row_el, col_el
        elif row_elements[col_el] == "x":
            total_targets += 1

for _ in range((int(input()))):
    command = input().split()
    action, direction = command[0], command[1]

    if action == "move":
        steps = int(command[2])
        next_row, next_col = take_next_steps(player_row, player_col, steps, direction)

        if is_outside(next_row, next_col, m_size):
            continue

        elif matrix[next_row][next_col] == ".":
            matrix[player_row][player_col] = "."
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = "A"


    elif action == "shoot":
        position_row, position_col = player_row, player_col
        while True:
            shoot_row, shoot_col = take_next_steps(position_row, position_col, 1, direction)

            if is_outside(shoot_row, shoot_col, m_size):
                break

            elif matrix[shoot_row][shoot_col] == "x":
                hit_targets += 1
                matrix[shoot_row][shoot_col] = "."
                target_coords.append([shoot_row, shoot_col])
                break

            position_row, position_col = shoot_row, shoot_col
        if total_targets - hit_targets < 1:
            break

if (total_targets - hit_targets) == 0:
    print(f"Training completed! All {hit_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - hit_targets} targets left.")
[print(entry) for entry in target_coords]