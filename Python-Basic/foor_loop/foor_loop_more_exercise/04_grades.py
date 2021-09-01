students = int(input())

top_students = 0
between_four = 0
between_three = 0
fail = 0
grade_counter = 0

for student in range(students):
    grade = float(input())
    grade_counter += grade

    if grade >= 5:
        top_students += 1
    elif 4 <= grade < 5:
        between_four += 1
    elif 3 <= grade < 4:
        between_three += 1
    elif grade < 3:
        fail += 1

top_students_percent = (top_students / students) * 100
between_four_percent = (between_four / students) * 100
between_three_percent = (between_three / students) * 100
fail_percent = (fail / students) * 100
average = grade_counter / students

print(f"Top students: {top_students_percent:.2f}%")
print(f"Between 4.00 and 4.99: {between_four_percent:.2f}%")
print(f"Between 3.00 and 3.99: {between_three_percent:.2f}%")
print(f"Fail: {fail_percent:.2f}%")
print(f"Average: {average:.2f}")