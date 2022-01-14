clothes_in_box = [int(num) for num in input().split()]
capacity_of_rack = int(input())

current_rack_cap = capacity_of_rack
rack_counter = 1

while clothes_in_box:
    cloth_to_take = clothes_in_box[-1]
    if current_rack_cap - cloth_to_take >= 0:
        clothes_in_box.pop()
        current_rack_cap -= cloth_to_take
    else:
        rack_counter += 1
        current_rack_cap = capacity_of_rack

print(rack_counter)