width = int(input())
length = int(input())
height = int(input())
number_of_boxes = int(input())

free_space_house = width * length * height
size_boxes = 0

meters_needed = 0

while True:
    if number_of_boxes == 'Done':
        break
    number_of_boxes = int(number_of_boxes)
    size_boxes += number_of_boxes
    if free_space_house < size_boxes:
        meters_needed = abs(free_space_house - size_boxes)
        print(f"No more free space! You need {meters_needed} Cubic meters more.")
        break
    number_of_boxes = input()

meters_needed = abs(free_space_house - size_boxes)

if free_space_house >= size_boxes:
    print(f"{meters_needed} Cubic meters left.")