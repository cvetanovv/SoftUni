class Party:

    def __init__(self):
        self.people = []


my_party = Party()
total_people = 0

while True:
    name = input()
    if name == "End":
        break
    my_party.people.append(name)
    total_people += 1

print(f"Going: {', '.join(my_party.people)}")
print(f"Total: {total_people}")
