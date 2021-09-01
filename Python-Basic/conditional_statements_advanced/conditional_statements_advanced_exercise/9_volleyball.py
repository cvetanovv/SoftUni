import math

kind_year = input()
holidays = int(input())
weekends_in_home = int(input())

weekends_play_in_sofia = (48 - weekends_in_home) * 3/4
games_in_holidays = holidays * 2/3
all_games = weekends_play_in_sofia + games_in_holidays + weekends_in_home

if kind_year == 'leap':
    all_games += all_games * 0.15

print(math.floor(all_games))
