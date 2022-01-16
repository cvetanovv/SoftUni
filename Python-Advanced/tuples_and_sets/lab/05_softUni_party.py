number_of_guest = int(input())

reservations = set()

for _ in range(number_of_guest):
    reservation = input()
    reservations.add(reservation)

guests_who_came_to_party = set()

guest = input()
while guest != "END":
    guests_who_came_to_party.add(guest)
    guest = input()

reservations.difference_update(guests_who_came_to_party)
guest_not_came = sorted(reservations)

print(len(reservations))
for res in guest_not_came:
    print(res)
