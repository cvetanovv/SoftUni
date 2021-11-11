number_of_iterations = int(input())

students = {}

for i in range(number_of_iterations):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)

average_grade_students = {}

for name, grades in students.items():
    av_grade = sum(grades) / len(grades)
    if av_grade >= 4.50:
        average_grade_students[name] = av_grade

sorted_average_grade = sorted(average_grade_students.items(), key=lambda kvp: -kvp[1])

for key, value in sorted_average_grade:
    print(f"{key} -> {value:.2f}")