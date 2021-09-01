number_of_cargos = int(input())

all_tone_cargo = 0
price = 0
minibus = 0
truck = 0
train = 0

for x in range(number_of_cargos):
    tone_cargo = int(input())
    all_tone_cargo += tone_cargo

    if tone_cargo <= 3:
        minibus += tone_cargo
    elif 4 <= tone_cargo <= 11:
        truck += tone_cargo
    elif tone_cargo >= 12:
        train += tone_cargo

price = ((minibus * 200) + (truck * 175) + (train * 120)) / all_tone_cargo
minibus_percent = (minibus / all_tone_cargo) * 100
truck_percent = (truck / all_tone_cargo) * 100
train_percent = (train / all_tone_cargo) * 100

print(f"{price:.2f}")
print(f"{minibus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")