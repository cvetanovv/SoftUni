courses = {}
needed_course = ''

while True:
    command = input()
    if ":" not in command:
        needed_course = command
        break
    command = command.split(":")
    name = command[0]
    id = command[1]
    course = command[2]

    if course not in courses:
        courses[course] = {}

    courses[course][name] = id

needed_course = needed_course.replace("_", " ")

for key, value in courses[needed_course].items():
    print(f"{key} - {value}")