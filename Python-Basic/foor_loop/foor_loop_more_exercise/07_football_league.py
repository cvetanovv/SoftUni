stadium_capacity = int(input())
all_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for fan in range(all_fans):
    sector = input()

    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    elif sector == 'G':
        sector_g += 1

sector_a_percent = sector_a / all_fans * 100
sector_b_percent = sector_b / all_fans * 100
sector_v_percent = sector_v / all_fans * 100
sector_g_percent = sector_g / all_fans * 100
all_fans_percent = all_fans / stadium_capacity * 100

print(f"{sector_a_percent:.2f}%")
print(f"{sector_b_percent:.2f}%")
print(f"{sector_v_percent:.2f}%")
print(f"{sector_g_percent:.2f}%")
print(f"{all_fans_percent:.2f}%")