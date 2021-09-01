height_house = float(input())
weight_side_walls = float(input())
height_roof = float(input())

def walls():
    side_wall = height_house * weight_side_walls
    window = 1.5 * 1.5
    side_walls = (2 * side_wall) - (2 * window)
    back_walls = height_house * height_house
    front_and_back_walls = (2 * back_walls) - (1.2 * 2)
    total_area = side_walls + front_and_back_walls
    green_paint = total_area / 3.4
    print(format(green_paint, '.2f'))

def roof():
    two_rectangle_roof = 2 * (height_house * weight_side_walls)
    two_triangles = 2 * (height_house * height_roof / 2)
    all_area = two_rectangle_roof + two_triangles
    red_paint = all_area / 4.3
    print((format(red_paint, '.2f')))

walls()
roof()