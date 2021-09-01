jury_number = int(input())

all_grade_point = 0
number_of_grades = 0

while True:
    presentation = input()
    if presentation == 'Finish':
        print(f"Student's final assessment is {all_grade_point / number_of_grades:.2f}.")
        break

    presentation_point = 0
    for jury in range(jury_number):
        grade = float(input())
        all_grade_point += grade
        presentation_point += grade
        number_of_grades += 1
    print(f"{presentation} - {presentation_point / jury_number:.2f}.")
