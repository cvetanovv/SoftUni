fires_with_cells = input().split("#")
water = int(input())
total_effort = 0
total_fire = 0

print("Cells:")
for fire in fires_with_cells:
    cells = fire.split(" = ")
    type_of_fire = cells[0]
    fire_level = int(cells[1])
    if water - fire_level >= 0:
        if type_of_fire == 'High':
            if 81 <= fire_level <= 125:
                print(f"- {fire_level}")
                water -= fire_level
                total_effort += fire_level * 0.25
                total_fire += fire_level
            else:
                continue
        elif type_of_fire == 'Medium':
            if 51 <= fire_level <= 80:
                print(f"- {fire_level}")
                water -= fire_level
                total_effort += fire_level * 0.25
                total_fire += fire_level
            else:
                continue
        elif type_of_fire == 'Low':
            if 1 <= fire_level <= 50:
                print(f"- {fire_level}")
                water -= fire_level
                total_effort += fire_level * 0.25
                total_fire += fire_level
            else:
                continue
    else:
        continue

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")