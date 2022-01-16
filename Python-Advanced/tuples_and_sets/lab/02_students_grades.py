number_of_students = int(input())

students_dict = {}

for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in students_dict:
        students_dict[name] = []
    students_dict[name].append(grade)

for student, grades in students_dict.items():
    sum_of_nums = sum(grades) / len(grades)
    formatted_grade = [f"{n:.2f}" for n in grades]
    print(f"{student} -> {' '.join(formatted_grade)} (avg: {sum_of_nums:.2f})")