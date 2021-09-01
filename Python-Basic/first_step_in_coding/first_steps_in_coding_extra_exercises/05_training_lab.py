long = float(input())
width = float(input())

width_cm = width * 100
room_long_cm = long * 100

room_width_minus_coridor = width_cm - 100
desks = room_width_minus_coridor // 70

rows_in_room = room_long_cm // 120

places_in_room = (desks * rows_in_room) - 3
print(int(places_in_room))