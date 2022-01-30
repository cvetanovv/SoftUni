from collections import deque

values_of_boxes_materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

crafted_items = {"Doll": 0, "Wooden train": 0, "Teddy bear": 0, "Bicycle": 0}

while True:
    if not values_of_boxes_materials or not magic_values:
        break
    box_with_material = values_of_boxes_materials.pop()
    magic_value = magic_values.popleft()

    if box_with_material * magic_value in presents:
        result = box_with_material * magic_value
        if result == 150:
            crafted_items["Doll"] += 1
        elif result == 250:
            crafted_items["Wooden train"] += 1
        elif result == 300:
            crafted_items["Teddy bear"] += 1
        elif result == 400:
            crafted_items["Bicycle"] += 1
        continue

    if box_with_material == 0 and magic_value == 0:
        continue
    elif box_with_material == 0:
        magic_values.appendleft(magic_value)
        continue
    elif magic_value == 0:
        values_of_boxes_materials.append(box_with_material)
        continue

    if box_with_material * magic_value < 0:
        result = box_with_material + magic_value
        values_of_boxes_materials.append(result)
        continue
    values_of_boxes_materials.append(box_with_material + 15)

if (crafted_items["Doll"] > 0 and crafted_items["Wooden train"] > 0) or (crafted_items["Teddy bear"] > 0 and crafted_items["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")


if values_of_boxes_materials:
    reversed_materials = reversed(values_of_boxes_materials)
    materials_left = ', '.join(str(x) for x in reversed_materials)
    print(f"Materials left: {materials_left}")

if magic_values:
    reversed_magic = magic_values
    magic_left = ', '.join(str(x) for x in reversed_magic)
    print(f"Magic left: {magic_left}")

sorted_crafted_items = sorted(crafted_items.items())

for item, value in sorted_crafted_items:
    if value > 0:
        print(f"{item}: {value}")