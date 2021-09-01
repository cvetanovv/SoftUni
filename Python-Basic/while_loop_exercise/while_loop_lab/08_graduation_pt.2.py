name = input()

grade = 1
total_rating = 0
number_of_fails = 0

while grade <= 12:
    yearly_rating = float(input())
    if yearly_rating < 4:
        number_of_fails += 1
        if number_of_fails == 2:
            break
    if yearly_rating >= 4:
        grade += 1
        total_rating += yearly_rating


average_grade = total_rating / 12

if number_of_fails >= 2:
    print(f"{name} has been excluded at {grade} grade")
else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")