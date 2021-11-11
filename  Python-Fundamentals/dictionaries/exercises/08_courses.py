courses = {}

while True:
    command = input()
    if command == "end":
        break
    command = command.split(" : ")
    course = command[0]
    name = command[1]
    if course not in courses:
        courses[course] = []

    courses[course].append(name)

sorted_courses = sorted(courses.items(), key=lambda kvp: -len(kvp[1]))

for course in sorted_courses:
    print(f"{course[0]}: {len(course[1])}")
    sorted_name = sorted(course[1])
    for name in sorted_name:
        print(f"-- {name}", end='\n')
