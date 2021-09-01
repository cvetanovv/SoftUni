import math

needed_hour = int(input())
firm_days_has = int(input())
workers_overtime = int(input())

working_hours = (firm_days_has * 0.90) * 8
working_hours_overtime = workers_overtime * (2 * firm_days_has)

together_hours = math.floor(working_hours + working_hours_overtime)

if needed_hour <= together_hours:
    left_hours = together_hours - needed_hour
    print(f"Yes!{left_hours} hours left.")
else:
    missing_hours = needed_hour - together_hours
    print(f"Not enough time!{missing_hours} hours needed.")