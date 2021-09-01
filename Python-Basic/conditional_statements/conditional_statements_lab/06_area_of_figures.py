import math
figure = input()

if figure == 'square':
    lenght = float(input())
    area = lenght * lenght
    print(f"{area:.3f}")

if figure == 'rectangle':
    first_lenght = float(input())
    second_lenght = float(input())
    area = first_lenght * second_lenght
    print(f"{area:.3f}")

if figure == 'circle':
    radius = float(input())
    area = math.pi * radius**2
    print(f"{area:.3f}")

if figure == 'triangle':
    lenght_side = float(input())
    lenght_height = float(input())
    area = (lenght_side / 2) * lenght_height
    print(f"{area:.3f}")