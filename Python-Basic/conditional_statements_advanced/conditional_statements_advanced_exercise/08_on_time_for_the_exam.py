hour_exam = int(input())
minutes_exam = int(input())
hour_coming = int(input())
minutes_coming = int(input())

exam_in_minutes = (hour_exam * 60) + minutes_exam
coming_in_minutes = (hour_coming * 60) + minutes_coming

diff = abs(exam_in_minutes - coming_in_minutes)
diff_in_hour = diff // 60
diff_in_minutes = diff % 60

if exam_in_minutes < coming_in_minutes:
    print('Late')
    if diff < 60:
        print(f"{diff} minutes after the start")
    elif diff >= 60:
        print(f"{diff_in_hour}:{diff_in_minutes:02} hours after the start")
elif diff <= 30:
    if exam_in_minutes == coming_in_minutes:
        print('On Time')
    else:
        print('On Time')
        print(f"{diff} minutes before the start")
elif diff > 30:
    print('Early')
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        print(f"{diff_in_hour}:{diff_in_minutes:02} hours before the start")