failed_threshold = int(input())

all_grades = 0
number_of_problems = 0
bad_grades = 0
last_problem = ''

while True:
    name_exercise = input()
    if name_exercise == 'Enough':
        average_scores = all_grades / number_of_problems
        print(f"Average score: {average_scores:.2f}")
        print(f"Number of problems: {number_of_problems}")
        print(f"Last problem: {last_problem}")
        break

    grade = int(input())

    if grade <= 4:
        bad_grades += 1

    if bad_grades == failed_threshold:
        print(f"You need a break, {bad_grades} poor grades.")
        break

    all_grades += grade
    number_of_problems += 1
    last_problem = name_exercise

