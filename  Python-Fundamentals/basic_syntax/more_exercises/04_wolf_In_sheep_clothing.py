sheep_list = input().split(", ")

wolf_position = 0

for index in range(len(sheep_list)):
    if sheep_list[index] == 'wolf':
        wolf_position = index
sheep_after_wolf = sheep_list[wolf_position:]

if sheep_list[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_after_wolf.count('sheep')}! You are about to be eaten by a wolf!")