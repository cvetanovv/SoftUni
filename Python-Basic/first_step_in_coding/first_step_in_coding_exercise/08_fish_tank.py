length = int(input())
width = int(input())
height = int(input())
precentage_ocupied_volume = float(input())

volume_aquarium = length * width * height
liters = volume_aquarium / 1000
precent = precentage_ocupied_volume / 100
needed_litres =liters * (1-precent)
print(needed_litres)