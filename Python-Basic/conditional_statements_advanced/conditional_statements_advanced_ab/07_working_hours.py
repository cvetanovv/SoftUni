hour = int(input())
day = input()

if day == 'Sunday':
    print('closed')
elif day in 'Monday	Tuesday	Wednesday Thursday Friday Saturday Sunday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')