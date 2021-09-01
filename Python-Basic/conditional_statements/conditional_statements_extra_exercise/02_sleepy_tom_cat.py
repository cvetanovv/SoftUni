not_working_days = int(input())
norm = 30000

minutes_plays_in_rest_days = not_working_days * 127
minutes_plays_in_working_days = (365 - not_working_days) * 63
full_year_minutes_plays = minutes_plays_in_rest_days + minutes_plays_in_working_days

if norm > full_year_minutes_plays:
    minutes_left = norm - full_year_minutes_plays
    hours = minutes_left // 60
    minutes = minutes_left % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    minutes_more = full_year_minutes_plays - norm
    hours = minutes_more // 60
    minutes = minutes_more % 60
    print('Tom will run away')
    print(f"{hours} hours and {minutes} minutes more for play")