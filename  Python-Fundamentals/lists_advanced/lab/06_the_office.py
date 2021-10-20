employees_happiness = [int(num) for num in input().split()]
happiness_improvement = int(input())

happiness_after_improvement = [employees * 3 for employees in employees_happiness]
sum_employees = sum(happiness_after_improvement)
length_employees = len(happiness_after_improvement)
average_happiness = sum_employees / length_employees

more_than_average_happy_employees = []

for employee in happiness_after_improvement:
    if employee >= average_happiness:
        more_than_average_happy_employees.append(employee)

if len(more_than_average_happy_employees) >= len(happiness_after_improvement) / 2:
    print(f"Score: {len(more_than_average_happy_employees)}/{length_employees}. Employees are happy!")
else:
    print(f"Score: {len(more_than_average_happy_employees)}/{length_employees}. Employees are not happy!")